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
import os
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

def run_reframe(
    args: list[str],
    env: dict[str, str] | None = None,
    verbose: bool = False,
) -> tuple[int, str, str]:
    """
    Executes the 'reframe' command as a subprocess.

    Args:
        args: A list of command-line arguments to pass to the 'reframe' executable.
        env: Optional dictionary of environment variables to provide to the subprocess.
        verbose: If True, prints debug information regarding the command, environment, and output.

    Returns:
        A tuple containing (returncode, stdout, stderr).

    Raises:
        SystemExit: If the 'reframe' executable is not found in the system PATH.
    """
    full_cmd = ["reframe", *args]
    if verbose:
        print(f"[DEBUG] Running command: {' '.join(full_cmd)}", flush=True)
    
    # Print environment variables if uenv-related ones are set
    if env and verbose:
        uenv_vars = {k: v for k, v in env.items() if 'UENV' in k or 'RFM' in k}
        if uenv_vars:
            print("[DEBUG] Environment variables set:", flush=True)
            for k, v in sorted(uenv_vars.items()):
                print(f"        {k}={v}", flush=True)
    
    try:
        p = subprocess.run(
            full_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env or os.environ.copy(),
        )
    except FileNotFoundError as e:
        print(f"\n[ERROR] Could not find 'reframe' command in PATH", flush=True)
        print(f"[ERROR] Error: {e}", flush=True)
        print(f"[DEBUG] Current PATH: {(env or os.environ).get('PATH', '(not set)')}", flush=True)
        raise SystemExit(
            f"ERROR: Could not find 'reframe' command in PATH.\n"
            f"Make sure ReFrame is installed and activated in your environment.\n"
            f"Current PATH: {(env or os.environ).get('PATH', '(not set)')}"
        )
    
    if verbose:
        print(f"[DEBUG] Return code: {p.returncode}", flush=True)
        print(f"[DEBUG] STDOUT length: {len(p.stdout)} chars", flush=True)
        print(f"[DEBUG] STDERR length: {len(p.stderr)} chars", flush=True)
        
        if p.stdout:
            print(f"[DEBUG] STDOUT (first 500 chars):\n{p.stdout[:500]}", flush=True)
        if p.stderr:
            print(f"[DEBUG] STDERR (first 500 chars):\n{p.stderr[:500]}", flush=True)
    
    return p.returncode, p.stdout, p.stderr


# -----------------------------------------------------------------------------
# Filename helpers
# -----------------------------------------------------------------------------

def sanitize_for_filename(s: str) -> str:
    """
    Sanitizes a string for safe use as a filename component.

    Replaces any character that is not alphanumeric, a period, an underscore, 
    or a hyphen with an underscore.

    Args:
        s: The input string to sanitize.

    Returns:
        A sanitized version of the string. Returns "unknown" if the resulting 
        string is empty.
    """
    s = (s or "").strip()
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s) or "unknown"


def truncate_filename_part(s: str, max_len: int = 60) -> str:
    """
    Truncates a string to a maximum length and removes trailing separators.

    Args:
        s: The input string to truncate.
        max_len: The maximum allowed length. Defaults to 60.

    Returns:
        The truncated string, with any trailing underscores, hyphens, or 
        periods removed to ensure a clean filename.
    """
    s = (s or "").strip()
    return s if len(s) <= max_len else s[:max_len].rstrip("_-.")


def extract_tag_from_extra(extra: list[str]) -> Optional[str]:
    """
    Extracts a tag expression from the list of passthrough arguments.

    Supports both '--tag=EXPR' and '--tag EXPR' (or '--tags EXPR') formats.

    Args:
        extra: A list of command-line arguments passed after the '--' separator.

    Returns:
        The extracted tag string if found; otherwise, None.
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
    """
    Normalizes passthrough arguments for ReFrame.

    Removes the leading '--' separator if present and strips any '--tag' or
    '--tags' arguments so that tags are not passed to ReFrame twice.

    Args:
        extra: A list of arguments passed after the '--' separator.

    Returns:
        A cleaned list of arguments ready for use in the Reint ReFrame command.
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
    """
    Creates an output path with a suffixed filename based on the provided filters.

    The generated filename follows this pattern:
    <stem>_<system>[_mode-<mode>][_tags-<tag>].md

    Args:
        base_output: The base filename or path (e.g., 'report.md').
        system: The ReFrame system name.
        mode: The execution mode (optional).
        tag: The tag expression (optional).
        output_dir: The directory where the file should be saved (optional).

    Returns:
        A Path object pointing to the newly constructed file.
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
    """
    Generates a path for the raw ReFrame output, mirroring the Markdown filename.

    The resulting filename uses the same base name as the Markdown file but 
    appends a '.reframe.out' suffix instead of '.md'.

    Args:
        md_path: The Path object of the Markdown report.

    Returns:
        A Path object pointing to the raw ReFrame output file.
    """
    name = md_path.name
    if name.lower().endswith(".md"):
        base = name[:-3]
    else:
        base = md_path.stem
    return md_path.with_name(f"{base}.reframe.out")


# -----------------------------------------------------------------------------
# Parsing helpers (JSON)
# -----------------------------------------------------------------------------

def parse_reframe_json(text: str, verbose: bool = False) -> list[dict]:
    """
    Parses the ReFrame '--describe' JSON output into a list of standardized dictionaries.

    This function is designed to be robust; it attempts to find the JSON array 
    within the text by locating the first '[' and the last ']', effectively 
    ignating any ReFrame log messages or headers that might precede the JSON.

    Args:
        text: The raw string output from the ReFrame command.
        verbose: If True, prints debug information about the parsing process.

    Returns:
        A list of dictionaries. Each dictionary contains:
            - 'kind': (str) Always "check" in this context.
            - 'display_name': (str) The name of the test.
            - 'hashcode': (str) The unique hashcode for the test.
            - 'file': (str) The path to the file where the test is defined.
            - 'description': (str) The description of the test.

    Raises:
        ValueError: If the JSON is malformed or cannot be extracted from the input.
    """
    if not text or not text.strip():
        if verbose:
            print("[DEBUG] parse_reframe_json: Empty or whitespace-only input", flush=True)
        return []

    if verbose:
        print(f"[DEBUG] parse_reframe_json: Input length = {len(text)} chars", flush=True)
        print(f"[DEBUG] parse_reframe_json: First 200 chars: {text[:200]}", flush=True)

    try:
        # ReFrame output might contain logging info before the actual JSON array.
        # Isolate the JSON array by finding the outermost brackets.
        start_idx = text.find('[')
        end_idx = text.rfind(']') + 1
        
        if verbose:
            print(f"[DEBUG] parse_reframe_json: Found '[' at {start_idx}, ']' at {end_idx-1}", flush=True)
        
        if start_idx != -1 and end_idx != 0:
            json_str = text[start_idx:end_idx]
            if verbose:
                print(f"[DEBUG] parse_reframe_json: Extracted JSON is {len(json_str)} chars", flush=True)
            raw_items = json.loads(json_str)
        else:
            if verbose:
                print(f"[DEBUG] parse_reframe_json: No brackets found, parsing entire text", flush=True)
            raw_items = json.loads(text)
        
        if verbose:
            print(f"[DEBUG] parse_reframe_json: Parsed {len(raw_items)} items from JSON", flush=True)
            
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON parse error: {e}", flush=True)
        print(f"[ERROR] Error at line {e.lineno}, col {e.colno}", flush=True)
        print(f"[ERROR] Text around error: {text[max(0, e.pos-100):e.pos+100]}", flush=True)
        raise ValueError(f"Failed to parse ReFrame JSON output: {e}\nOutput was: {text[:500]}...")

    items = []
    for i, item in enumerate(raw_items):
        parsed_item = {
            "kind": "check",
            "display_name": item.get("display_name", ""),
            "hashcode": item.get("hashcode", ""),
            "file": item.get("@file", ""),
            "description": item.get("descr", ""),
        }
        if verbose:
            print(f"[DEBUG] Item {i}: {parsed_item['display_name']}", flush=True)
        items.append(parsed_item)
        
    return items


# -----------------------------------------------------------------------------
# Markdown output helpers
# -----------------------------------------------------------------------------

def normalize_table_cell(text: str | None) -> str:
    """
    Formats a string to be safe for use within a Markdown table cell.

    The function performs the following transformations:
    1. Converts `None` or empty strings to a dash ("—").
    2. Normalizes all types of newlines to `\n`.
    3. Replaces `\n` with HTML `<br>` tags to allow multi-line content in a single cell.
    4. Escapes the pipe character (`|`) to prevent breaking the Markdown table structure.

    Args:
        text: The input string to format.

    Returns:
        A sanitized, Markdown-compatible string.
    """
    if not text:
        return "—"
    s = str(text).replace("\r\n", "\n").replace("\r", "\n").strip()
    if not s:
        return "—"
    s = s.replace("\n", "<br>")
    return s.replace("|", r"\|")


def split_name_and_params(name: str) -> tuple[str, list[str]]:
    """
    Splits a test display name into its base name and its associated parameters.

    The function identifies parameters starting with a '%' character and 
    captures everything until the next '%' or the end of the string.

    Args:
        name: The display name string (e.g., "test_name %param1=val1 %param2=val:val2").

    Returns:
        A tuple containing:
        - The base name (str): The name with all parameter tokens removed.
        - The parameters (list[str]): A list of the extracted tokens (e.g., ['%param1=val1', ...]).
    """
    s = (name or "").strip()
    if not s:
        return "—", []

    params = re.findall(r"%.*?(?=\s%|$)", s)
    base = re.sub(r"\s*%.*?(?=\s%|$)", "", s).strip()
    return (base if base else s, params)


def params_inline_lines(params: list[str]) -> str:
    """
    Converts a list of parameters into a single string of HTML-formatted bullet points.

    This is used to display multiple parameters within a single Markdown table cell,
    using `<br>• ` to create a vertical list effect.

    Args:
        params: A list of parameter strings (e.g., ['%param1=val1', '%param2=val2']).

    Returns:
        A single string containing the bulleted parameters, or an empty string 
        if the input list is empty.
    """
    if not params:
        return ""
    return "".join(f"<br>• {normalize_table_cell(p)}" for p in params)


def checks_relative_path(file_path: str) -> Optional[str]:
    """
    Extracts the portion of a file path relative to the 'checks/' directory.

    This helps in normalizing paths so that the report focuses on the 
    internal project structure rather than absolute system paths.

    Args:
        file_path: The full or partial path to the test file.

    Returns:
        A string representing the path starting from 'checks/...' 
        (e.g., 'checks/cpu/test.py'), or None if 'checks/' is not found in the path.
    """
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
    """
    Determines the category path from a relative 'checks/' path string.

    If the path starts with 'checks/', this function extracts the subdirectories
    located between 'checks/' and the final filename.

    Args:
        rel: A relative path string (e.g., 'checks/system/gssr/test.py').

    Returns:
        A string of the category subfolders (e.g., 'system/gssr'), or '—' 
        if the path is invalid or contains no intermediate folders.
    """
    if not rel:
        return "—"
    parts = rel.split("/")
    if len(parts) < 2 or parts[0] != "checks":
        return "—"
    folders = parts[1:-1]
    return "/".join(folders) if folders else "—"


def md_link(text: str, href: str) -> str:
    """
    Creates a standard Markdown hyperlink.

    Args:
        text: The display text to be shown in the link.
        href: The URL or file path for the link destination.

    Returns:
        A string formatted as '[text](href)'.
    """
    return f"[{text}]({href})"


def category_cell(file_path: str | None) -> str:
    """
    Generates a Markdown hyperlink for the test category based on the file path.

    The link target is constructed as `../checks/<category>/`, where `<category>`
    is the subfolder structure found within the 'checks/' directory.

    Args:
        file_path: The path to the test file.

    Returns:
        A Markdown link to the category directory, or "—" if no valid
        category can be extracted from the path.
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
    Formats the test name for display in a Markdown table cell.

    The function extracts parameters from the display name, adds a prefix 
    ("↳ ") if the test is of kind "related", and creates a hyperlink 
    to the source file if a valid path is provided.

    Args:
        display_name: The raw name of the test (including any %param tokens).
        kind: The classification of the test (e.g., "check" or "related").
        file_path: The file path where the test is defined.

    Returns:
        A Markdown-formatted string containing the linked name and 
        parameter bullets underneath.
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
    """
    Constructs the Markdown preamble section containing report metadata.

    This section lists the filters used (system, mode, tags), the total
    number of tests found, and the timestamp of when the report was generated.

    Args:
        system: The ReFrame system name.
        mode: The execution mode (optional).
        tag: The tag expression (optional).
        found: The number of tests matched by the filters (optional).

    Returns:
        A string formatted as a Markdown-compatible list of metadata.
    """
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
    """
    Generates and writes the final Markdown report to the specified path.

    This function constructs the Markdown table by iterating through the 
    provided test items, formatting each row with the test name, 
    description, and category, and then writes the complete content to disk.

    Args:
        items: A list of dictionaries containing the parsed ReFrame test data.
        output_path: The Path object where the Markdown file will be saved.
        system: The ReFrame system name.
        mode: The execution mode used for the report.
        tag: The tag expression used for the report.
        found_count: The total number of tests found during the execution.

    Returns:
        None
    """
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


def run_matrix_mode(args, env: dict[str, str] | None = None):
    """
    Executes the logic for generating a "Matrix Mode" report.

    This function iterates through a list of specified targets (defined via
    '--matrix-mode' or '--matrix-tag'), runs 'reframe --describe' for each,
    and aggregates the results to create a cross-referenced Markdown table.
    The final report shows which tests are present/eligible in each target
    column, organized by their directory category, and includes a summary 
    of total counts per target.

    Args:
        args: The parsed command-line arguments (argparse.Namespace).
        env: Optional dictionary of environment variables to use when
             running the ReFrame subprocess.

    Returns:
        None
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
            if label in labels:
                raise ValueError(
                    f"duplicate label '{label}' in --matrix-mode/--matrix-tag"
                )
            targets.append((label, system, mode, None))
            labels.append(label)

    if args.matrix_tag:
        for t in args.matrix_tag:
            parts = t.split(":")
            if len(parts) != 3:
                raise ValueError("--matrix-tag requires label:system:tag")

            label, system, tag = parts
            if label in labels:
                raise ValueError(
                    f"duplicate label '{label}' in --matrix-mode/--matrix-tag"
                )
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
        if args.verbose:
            cmd.insert(1, "-v")
        if mode:
            cmd += ["--mode", mode]
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

        rc, out, err = run_reframe(base_args + cmd + cleaned_extra, env=env, verbose=args.verbose)

        if rc != 0:
            msg = (
                f"[ERROR] reframe exited with code {rc}; "
                f"skipping target {label}"
            )
            print(msg)
            if err:
                print("[ERROR] STDERR output:", flush=True)
                print(err, flush=True)
            if out:
                print("[ERROR] STDOUT output (first 500 chars):", flush=True)
                print(out[:500], flush=True)
            continue

        items = parse_reframe_json(out, verbose=args.verbose)

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
    """
    The main entry point of the script.

    This function performs the following high-level steps:
    1. Parses and validates command-line arguments using argparse.
    2. Validates existence of provided file paths and configuration directories.
    3. Configures the environment variables required for UENV-specific 
       ReFrame execution (e.g., RFM_UENV_RECIPES_DIR).
    4. Determines the execution mode:
       - Matrix Mode: If '--matrix-mode' or '--matrix-tag' are provided, 
         it delegates execution to `run_matrix_mode`.
       - Single Target Mode: Otherwise, it constructs a single 'reframe --describe' 
         command for a specific system/mode/tag and generates a standard report.
    5. Orchestrates the execution of the ReFrame command, handles potential 
       subprocess errors, and writes the final Markdown report(s) to disk.

    Raises:
        SystemExit: If required arguments are missing, if provided paths do 
                    not exist, or if the ReFrame command fails.
    """
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
        "--uenv-recipes-dir",
        default=None,
        help=(
            "Path to local UENV recipe metadata for listing UENV tests "
            "without installed uenv images."
        ),
    )
    ap.add_argument(
        "--uenv-image-inventory",
        default=None,
        help=(
            "Path to a UENV image inventory JSON file produced by "
            "`uenv image find --json`. This is used to map local recipe "
            "metadata to available target systems."
        ),
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
    ap.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Pass -v to ReFrame for verbose output (useful for debugging)",
    )
    ap.add_argument("extra", nargs=argparse.REMAINDER,
                    help="Extra args passed to ReFrame after '--'")

    args = ap.parse_args()

    extra = normalize_extra_args(list(args.extra))

    if not args.matrix_mode and not args.matrix_tag and not args.system:
        raise SystemExit(
            "--system is required unless using --matrix-mode or --matrix-tag"
        )

    if args.uenv_image_inventory and not args.uenv_recipes_dir:
        raise SystemExit(
            "--uenv-image-inventory requires --uenv-recipes-dir"
        )

    # Validate uenv file paths
    if args.uenv_recipes_dir:
        recipes_path = Path(args.uenv_recipes_dir)
        if not recipes_path.exists():
            raise SystemExit(
                f"ERROR: --uenv-recipes-dir path does not exist: {args.uenv_recipes_dir}\n"
                f"Absolute path: {recipes_path.resolve()}"
            )
        print(f"[INFO] UENV recipes dir: {recipes_path.resolve()}")

    if args.uenv_image_inventory:
        inv_path = Path(args.uenv_image_inventory)
        if not inv_path.exists():
            raise SystemExit(
                f"ERROR: --uenv-image-inventory path does not exist: {args.uenv_image_inventory}\n"
                f"Absolute path: {inv_path.resolve()}"
            )
        print(f"[INFO] UENV image inventory: {inv_path.resolve()}")

    # -------------------------------------------
    # MATRIX MODE
    # -------------------------------------------
    subprocess_env = None
    if args.uenv_recipes_dir or args.uenv_image_inventory:
        subprocess_env = os.environ.copy()
        if args.uenv_recipes_dir:
            recipes_abs = Path(args.uenv_recipes_dir).resolve()
            subprocess_env["RFM_UENV_RECIPES_DIR"] = str(recipes_abs)
            if args.verbose:
                print(f"[DEBUG] Setting RFM_UENV_RECIPES_DIR={recipes_abs}")
        if args.uenv_image_inventory:
            inv_abs = Path(args.uenv_image_inventory).resolve()
            subprocess_env["RFM_UENV_IMAGE_INVENTORY"] = str(inv_abs)
            if args.verbose:
                print(f"[DEBUG] Setting RFM_UENV_IMAGE_INVENTORY={inv_abs}")

        if args.uenv_recipes_dir and not args.uenv_image_inventory:
            if args.matrix_mode or args.matrix_tag:
                systems = []
                if args.matrix_mode:
                    systems += [t.split(':')[1] for t in args.matrix_mode if ':' in t]
                if args.matrix_tag:
                    systems += [t.split(':')[1] for t in args.matrix_tag if ':' in t]
                systems = [s for s in dict.fromkeys(systems) if s]
                if systems:
                    subprocess_env["RFM_UENV_TARGET_SYSTEMS"] = ",".join(systems)
                    if args.verbose:
                        print(
                            f"[DEBUG] Setting RFM_UENV_TARGET_SYSTEMS={subprocess_env['RFM_UENV_TARGET_SYSTEMS']}"
                        )
            else:
                subprocess_env["RFM_UENV_TARGET_SYSTEMS"] = args.system
                if args.verbose:
                    print(
                        f"[DEBUG] Setting RFM_UENV_TARGET_SYSTEMS={args.system}"
                    )

    if args.matrix_mode or args.matrix_tag:
        run_matrix_mode(args, subprocess_env)
        return

    tag_used = args.tag if args.tag else extract_tag_from_extra(extra)

    # Build ReFrame args using --describe instead of -L
    reframe_args: list[str] = ["--describe"]
    if args.verbose:
        reframe_args.append("-v")
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
    rc, out, err = run_reframe(reframe_args, env=subprocess_env, verbose=args.verbose)
    combined = (out or "") + "\n" + (err or "")

    if rc != 0:
        print("\n" + "="*80, flush=True)
        print("[ERROR] ReFrame exited with code: {}".format(rc), flush=True)
        print("="*80, flush=True)
        print("\n[DEBUG] Full STDOUT output:", flush=True)
        print("-" * 40, flush=True)
        if out:
            print(out, flush=True)
        else:
            print("(empty)", flush=True)
        print("-" * 40, flush=True)
        print("\n[DEBUG] Full STDERR output:", flush=True)
        print("-" * 40, flush=True)
        if err:
            print(err, flush=True)
        else:
            print("(empty)", flush=True)
        print("-" * 40, flush=True)
        
        # Try to save raw output to a debug file
        debug_out_path = Path("debug_reframe_output.log")
        try:
            debug_out_path.write_text(
                f"Command: reframe {' '.join(reframe_args)}\n"
                f"Return code: {rc}\n\n"
                f"STDOUT:\n{out}\n\n"
                f"STDERR:\n{err}\n",
                encoding="utf-8"
            )
            print(f"\n[DEBUG] Full output saved to: {debug_out_path.resolve()}", flush=True)
        except Exception as e:
            print(f"\n[ERROR] Failed to save debug output: {e}", flush=True)
        
        raise SystemExit(
            "ReFrame failed.\n\n"
            + "Command: reframe "
            + " ".join(shlex.quote(x) for x in reframe_args)
            + "\n\nSTDERR:\n"
            + (err or "(empty)")
            + "\n\nSTDOUT (first 500 chars):\n"
            + (out[:500] if out else "(empty)")
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
    items = parse_reframe_json(out, verbose=args.verbose)
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
