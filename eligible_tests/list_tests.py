#!/usr/bin/env python3
"""
Generate a Markdown report by running and parsing ReFrame `--describe`.

Why parsing JSON?
- `reframe --describe` applies the exact selection logic
    (system/mode/tags/prgenv/etc.) and outputs the matched tests in JSON format.
    See ReFrame docs for details:
    https://reframe-hpc.readthedocs.io/en/v3.5.0/manpage.html
- We simply format what ReFrame outputs, rather than
    re-implementing filtering.
"""

import argparse
import json
import re
import shlex
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional
from urllib.parse import quote


# -----------------------------------------------------------------------------
# Running ReFrame
# -----------------------------------------------------------------------------

def run_reframe(args: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(
        ["reframe", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return p.returncode, p.stdout, p.stderr


# -----------------------------------------------------------------------------
# Filename helpers
# -----------------------------------------------------------------------------

def sanitize_for_filename(s: str) -> str:
    s = (s or "").strip()
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s) or "unknown"


def truncate_filename_part(s: str, max_len: int = 60) -> str:
    s = (s or "").strip()
    return s if len(s) <= max_len else s[:max_len].rstrip("_-.")


def extract_tag_from_extra(extra: list[str]) -> Optional[str]:
    """Extract `--tag` from passthrough args.

    Supports both `--tag=EXPR` and `--tag EXPR` forms.
    """
    if not extra:
        return None

    for i, t in enumerate(extra):
        if t.startswith("--tag="):
            return t.split("=", 1)[1]
        if t in ("--tag", "--tags") and i + 1 < len(extra):
            return extra[i + 1]
    return None


def normalize_extra_args(extra: list[str]) -> list[str]:
    """Normalize passthrough args for ReFrame.

    This removes a leading `--` separator and strips any `--tag` or
    `--tags` arguments so tags are not passed twice.
    """
    if extra and extra[0] == "--":
        extra = extra[1:]

    cleaned = []
    skip_next = False

    for arg in extra:
        if skip_next:
            skip_next = False
            continue
        if arg.startswith("--tag="):
            continue
        if arg in ("--tag", "--tags"):
            skip_next = True
            continue
        cleaned.append(arg)

    return cleaned


def build_output_path(
    base_output: str,
    system: str,
    mode: Optional[str],
    tag: Optional[str],
    output_dir: Optional[str] = None,
) -> Path:
    """Create an output path with a suffixed filename.

    The filename will be: <stem>_<system>[_mode-<mode>][_tags-<tag>].md
    """
    script_dir = Path(__file__).resolve().parent
    out_dir = Path(output_dir) if output_dir else script_dir

    p = Path(base_output)
    stem = p.stem if p.suffix else p.name
    ext = p.suffix if p.suffix else ".md"

    parts = [sanitize_for_filename(system)]
    if mode:
        parts.append(
            "mode-"
            + truncate_filename_part(sanitize_for_filename(mode))
        )
    if tag:
        parts.append(
            "tags-"
            + truncate_filename_part(sanitize_for_filename(tag))
        )

    suffix = "_".join(parts)
    filename = f"{stem}_{suffix}{ext}"
    return out_dir / filename


def build_reframe_out_path(md_path: Path) -> Path:
    """Same filename as the Markdown file, but with '.reframe.out' suffix."""
    name = md_path.name
    if name.lower().endswith(".md"):
        base = name[:-3]
    else:
        base = md_path.stem
    return md_path.with_name(f"{base}.reframe.out")


# -----------------------------------------------------------------------------
# Parsing helpers (JSON)
# -----------------------------------------------------------------------------

def parse_reframe_json(text: str) -> list[dict]:
    """
    Parse ReFrame --describe JSON output into a list of items.
    """
    if not text or not text.strip():
        return []

    try:
        # ReFrame output might contain logging info before the actual JSON array.
        # Isolate the JSON array by finding the outermost brackets.
        start_idx = text.find('[')
        end_idx = text.rfind(']') + 1
        
        if start_idx != -1 and end_idx != 0:
            json_str = text[start_idx:end_idx]
            raw_items = json.loads(json_str)
        else:
            raw_items = json.loads(text)
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse ReFrame JSON output: {e}\nOutput was: {text[:300]}...")

    items = []
    for item in raw_items:
        items.append({
            "kind": "check",
            "display_name": item.get("display_name", ""),
            "hashcode": item.get("hashcode", ""),
            "file": item.get("@file", ""),
            "description": item.get("descr", ""),
        })
        
    return items


# -----------------------------------------------------------------------------
# Markdown output helpers
# -----------------------------------------------------------------------------

def normalize_table_cell(text: str | None) -> str:
    """Table-safe: no physical newlines; escape pipes."""
    if not text:
        return "—"
    s = str(text).replace("\r\n", "\n").replace("\r", "\n").strip()
    if not s:
        return "—"
    s = s.replace("\n", "<br>")
    return s.replace("|", r"\|")


def split_name_and_params(name: str) -> tuple[str, list[str]]:
    """Extract %param=value tokens from display_name."""
    s = (name or "").strip()
    if not s:
        return "—", []

    params = re.findall(r"%.*?(?=\s%|$)", s)
    base = re.sub(r"\s*%.*?(?=\s%|$)", "", s).strip()
    return (base if base else s, params)


def params_inline_lines(params: list[str]) -> str:
    """Render params as <br> bullet lines."""
    if not params:
        return ""
    return "".join(f"<br>• {normalize_table_cell(p)}" for p in params)


def checks_relative_path(file_path: str) -> Optional[str]:
    """Return relative path starting at checks/"""
    if not file_path:
        return None
    norm = file_path.replace("\\", "/")
    idx = norm.find("/checks/")
    if idx >= 0:
        return norm[idx + 1:]
    idx = norm.find("checks/")
    if idx >= 0:
        return norm[idx:]
    return None


def category_from_checks_rel(rel: Optional[str]) -> str:
    if not rel:
        return "—"
    parts = rel.split("/")
    if len(parts) < 2 or parts[0] != "checks":
        return "—"
    folders = parts[1:-1]
    return "/".join(folders) if folders else "—"


def md_link(text: str, href: str) -> str:
    """Markdown link helper."""
    return f"[{text}]({href})"


def category_cell(file_path: str | None) -> str:
    """
    Category display: only the subfolders after checks/ (e.g. system/gssr)
    Hyperlink target: ../checks/<category>/
    """
    rel = checks_relative_path(file_path) if file_path else None
    category = category_from_checks_rel(rel)
    if not category or category == "—":
        return "—"

    href = quote(f"../checks/{category}/", safe="/._-")
    return md_link(normalize_table_cell(category), href)


def test_name_cell(
    display_name: str,
    kind: str,
    file_path: Optional[str],
) -> str:
    """
    Show the actual test name (not filename), with parameter bullets
    underneath. The test name itself is linked to the check's defining file
    (../checks/.../file.py).
    """
    base, params = split_name_and_params(display_name)
    prefix = "↳ " if kind == "related" else ""

    link_text = normalize_table_cell(prefix + base)
    bullets = params_inline_lines(params)

    rel = checks_relative_path(file_path) if file_path else None
    if rel and rel.startswith("checks/"):
        href = quote(f"../{rel}", safe="/._-")
        return md_link(link_text, href) + bullets

    # Fallback: no file path detected
    return link_text + bullets


def build_preamble(
    system: str,
    mode: Optional[str],
    tag: Optional[str],
    found: Optional[int],
) -> str:
    lines = ["- Filters:"]
    lines.append(f"  - system: `{system}`")
    if mode:
        lines.append(f"  - mode: `{mode}`")
    if tag:
        lines.append(f"  - tags: `{tag}`")
    lines.append(f"  - checks: `{found if found is not None else '—'}`")
    ts = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    lines.append(f"- Generated: `{ts}`")
    return "\n".join(lines)


def write_markdown(items: list[dict],
                   output_path: Path,
                   system: str,
                   mode: Optional[str],
                   tag: Optional[str],
                   found_count: Optional[int]):
    lines = [
        f"## Eligible ReFrame Tests on {system}",
        "",
        build_preamble(system, mode, tag, found_count),
        "",
        "| Test name | Description | Category |",
        "|----------|-------------|----------|",
    ]

    for it in items:
        file_path = it.get("file")
        display = it.get("display_name") or "—"
        name_cell = test_name_cell(display, it["kind"], file_path)
        desc_cell = normalize_table_cell(it.get("description") or "—")
        cat_cell = category_cell(file_path)

        lines.append(f"| {name_cell} | {desc_cell} | {cat_cell} |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run_matrix_mode(args):
    """
    Matrix mode: build a cross-system view of eligible tests.
    """

    print("[INFO] Running matrix mode")

    base_args = []

    for c in args.config_files:
        base_args += ["-C", c]

    for c in args.check_paths:
        base_args += ["-c", c]

    if args.recursive:
        base_args.append("-R")

    targets = []
    labels = []

    # -------------------------------------------
    # Build target list (explicit mode vs tag)
    # -------------------------------------------
    if args.matrix_mode:
        for t in args.matrix_mode:
            parts = t.split(":")
            if len(parts) != 3:
                raise ValueError("--matrix-mode requires label:system:mode")

            label, system, mode = parts
            targets.append((label, system, mode, None))
            labels.append(label)

    if args.matrix_tag:
        for t in args.matrix_tag:
            parts = t.split(":")
            if len(parts) != 3:
                raise ValueError("--matrix-tag requires label:system:tag")

            label, system, tag = parts
            targets.append((label, system, None, tag))
            labels.append(label)

    # -------------------------------------------
    # Collect data from ReFrame runs
    # -------------------------------------------
    all_tests = {}
    matrix = {}

    for label, system, mode, tag in targets:
        print(f"[INFO] Collecting target: {label}")
        print(f"       system={system}, mode={mode}, tag={tag}")

        cmd = ["--describe", "--system", system]
        if mode:
            cmd += ["-m", mode]
        if tag:
            cmd += ["--tag", tag]

        extra = list(args.extra or [])
        if extra and extra[0] == "--":
            extra = extra[1:]

        cleaned_extra = []
        skip_next = False
        for i, e in enumerate(extra):
            if skip_next:
                skip_next = False
                continue
            if e.startswith("--tag="):
                continue
            if e in ("--tag", "--tags"):
                skip_next = True
                continue
            cleaned_extra.append(e)

        full_cmd = ["reframe"] + base_args + cmd + cleaned_extra
        print("[CMD] " + " ".join(full_cmd))

        rc, out, err = run_reframe(base_args + cmd + cleaned_extra)

        if rc != 0:
            msg = (
                f"[ERROR] reframe exited with code {rc}; "
                f"skipping target {label}"
            )
            print(msg)
            if err:
                print(err)
            continue

        items = parse_reframe_json(out)

        for item in items:
            name = item["display_name"]

            if name not in all_tests:
                all_tests[name] = item

            matrix.setdefault(name, {})
            matrix[name][label] = True

    # -------------------------------------------
    # Group tests by category
    # -------------------------------------------
    categories = {}

    for name, item in all_tests.items():
        rel = checks_relative_path(item.get("file"))
        cat = category_from_checks_rel(rel)

        categories.setdefault(cat, []).append(name)

    # -------------------------------------------
    # Output path
    # -------------------------------------------
    output_path = build_output_path(
        args.filename,
        "matrix",
        None,
        None,
        args.output_dir,
    )

    print(f"[INFO] Writing matrix report: {output_path}")

    # -------------------------------------------
    # Build markdown
    # -------------------------------------------
    ts = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")

    lines = [
        "## Test Coverage Matrix",
        "",
        f"- Generated: `{ts}`",
        "",
    ]

    totals = {label: 0 for label in labels}

    for cat, tests in sorted(categories.items()):
        lines.append(f"### {cat}")
        lines.append("")

        header = "| Test name | " + " | ".join(labels) + " |"
        sep = "|-----------|" + "-----------|" * len(labels)

        lines.append(header)
        lines.append(sep)

        for name in sorted(tests):
            item = all_tests[name]

            cell = test_name_cell(
                item["display_name"],
                item["kind"],
                item.get("file")
            )

            row = [cell]

            for label in labels:
                val = matrix[name].get(label)
                if val:
                    totals[label] += 1
                row.append("✅" if val else "❌")

            lines.append("| " + " | ".join(row) + " |")

        lines.append("")

    lines.append("")
    lines.append("### Summary")
    lines.append("")

    summary_header = "| Metric | " + " | ".join(labels) + " |"
    summary_sep = "|--------|" + "--------|" * len(labels)

    lines.append(summary_header)
    lines.append(summary_sep)

    summary_row = (
        "| TOTAL | "
        + " | ".join(str(totals[label]) for label in labels)
        + " |"
    )
    lines.append(summary_row)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print("[INFO] Matrix generation complete")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=(
            "Generate Markdown report by parsing ReFrame `--describe` JSON output."
        )
    )
    ap.add_argument("--system", help="ReFrame system name (e.g. daint)")
    ap.add_argument("--mode", help="ReFrame execution mode (passed through)")
    ap.add_argument(
        "--tag",
        "--tags",
        dest="tag",
        help="Tag expression to pass to ReFrame (optional)",
    )
    ap.add_argument("-C", dest="config_files", action="append", default=[],
                    help="ReFrame config file (repeatable: -C a.py -C b.py)")
    ap.add_argument("-c", dest="check_paths", action="append", default=[],
                    help="Check path(s) (repeatable, passed through)")
    ap.add_argument("-R", dest="recursive", action="store_true",
                    help="Pass -R to ReFrame")
    ap.add_argument(
        "-f",
        "--filename",
        default="eligible_tests.md",
        help="Base output filename (suffixes added automatically).",
    )
    ap.add_argument(
        "-o",
        "--output_dir",
        default=None,
        help="Output directory for the report (default: script directory).",
    )
    ap.add_argument(
        "--matrix-mode",
        action="append",
        help="Matrix entry: label:system:mode",
    )
    ap.add_argument(
        "--matrix-tag",
        action="append",
        help="Matrix entry: label:system:tag",
    )
    ap.add_argument("extra", nargs=argparse.REMAINDER,
                    help="Extra args passed to ReFrame after '--'")

    args = ap.parse_args()

    extra = normalize_extra_args(list(args.extra))

    if not args.matrix_mode and not args.matrix_tag and not args.system:
        raise SystemExit(
            "--system is required unless using --matrix-mode or --matrix-tag"
        )

    # -------------------------------------------
    # MATRIX MODE
    # -------------------------------------------
    if args.matrix_mode or args.matrix_tag:
        run_matrix_mode(args)
        return

    tag_used = args.tag if args.tag else extract_tag_from_extra(extra)

    # Build ReFrame args using --describe instead of -L
    reframe_args: list[str] = ["--describe"]
    for cf in args.config_files:
        reframe_args.extend(["-C", cf])
    for cp in args.check_paths:
        reframe_args.extend(["-c", cp])
    if args.recursive:
        reframe_args.append("-R")
    reframe_args.extend(["--system", args.system])
    if args.mode:
        reframe_args.extend(["--mode", args.mode])
    if tag_used:
        reframe_args.append(f"--tag={tag_used}")
    reframe_args.extend(extra)

    print("[CMD] reframe " + " ".join(shlex.quote(x) for x in reframe_args))
    rc, out, err = run_reframe(reframe_args)
    combined = (out or "") + "\n" + (err or "")

    if rc != 0:
        raise SystemExit(
            "ReFrame failed.\n\n"
            + "Command: reframe "
            + " ".join(shlex.quote(x) for x in reframe_args)
            + "\n\nSTDERR:\n"
            + (err or "")
        )

    # Output paths
    md_path = build_output_path(
        args.filename,
        args.system,
        args.mode,
        tag_used,
        args.output_dir,
    )
    out_path = build_reframe_out_path(md_path)

    md_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(combined, encoding="utf-8")

    # Parse JSON output and determine count
    items = parse_reframe_json(out)
    found = len(items)

    write_markdown(
        items=items,
        output_path=md_path,
        system=args.system,
        mode=args.mode,
        tag=tag_used,
        found_count=found
    )

    print(f"Markdown written to {md_path}")
    print(f"ReFrame output saved to {out_path}")
    print(f"Checks (ReFrame --describe): {found}")


if __name__ == "__main__":
    main()