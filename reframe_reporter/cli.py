import argparse
from pathlib import Path
from typing import List, Tuple, NamedTuple
from .models import ReFrameReporterConfig
from .orchestrator import ReportOrchestrator


class ParsedArgs(NamedTuple):
    """Structured container for arguments parsed from the CLI."""
    config: ReFrameReporterConfig
    system: str
    mode: str
    tag: str
    extra_args: List[str]


def parse_args() -> Tuple[ParsedArgs, argparse.Namespace]:
    parser = argparse.ArgumentParser(description="ReFrame Test Reporter CLI")
    parser.add_argument("--uenv-recipes-dir", type=str, help="Directory containing UEnv recipes")
    parser.add_argument("-C", "--checks", action='append', default=[], help="Path to ReFrame config file or directory of checks")
    parser.add_argument("--system", type=str, required=False, help="ReFrame system name (e.g., daint)")
    parser.add_argument("--mode", type=str, default="single", help="ReFrame execution mode")
    parser.add_argument("--tag", "--tags", dest="tag", help="Tag expression to pass to ReFrame")
    parser.add_argument("-c", "--config_dir", type=str, help="Directory containing test configs (passed via extra args)")
    parser.add_argument("-R", "--recursive", action="store_true", help="Recursive mode")
    parser.add_argument("-f", "--filename", default="eligible_tests.md", help="Base output filename")
    parser.add_argument("-o", "--output_dir", type=str, help="Output directory for the report")
    parser.add_argument("--uenv-image-inventory", type=str, help="Path to UHM image inventory JSON")
    parser.add_argument("--matrix-mode", type=str, help="Comma-separated matrix entries: label:system:mode,label2:system2:mode")
    parser.add_argument("--matrix-tag", action='append', help="Matrix entry: label:arg")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("extra", nargs=argparse.REMAINDER, help="Extra args passed to ReFrame after '--'")

    args = parser.parse_args()

    reconstructed_extra = []
    for check in args.checks:
        reconstructed_extra.extend(["-C", str(Path(check).resolve())])
    if args.config_dir:
        reconstructed_extra.extend(["-c", str(Path(args.config_dir).resolve())])

    out_dir = Path(args.output_dir) if args.output_dir else Path.cwd()
    tag_val = args.tag if args.tag else ""

    config = ReFrameReporterConfig(
        config_files=[Path(c) for c in args.checks],
        check_paths=[Path(p) for p in args.checks] if args.checks else [], 
        recursive=args.recursive,
        uenv_recipes_dir=Path(args.uenv_recipes_dir) if args.uenv_recipes_dir else None,
        uenv_image_inventory=Path(args.uenv_image_inventory) if args.uenv_image_inventory else None,
        uenv_env={}, 
        output_dir=out_dir,
        filename=args.filename,
        system=args.system or "",
        mode=args.mode,
        tag=tag_val
    )

    parsed = ParsedArgs(
        config=config,
        system=args.system or "",
        mode=args.mode,
        tag=tag_val,
        extra_args=reconstructed_extra
    )

    return parsed, args

def main():
    try:
        parsed, args = parse_args()
        orchestrator = ReportOrchestrator(parsed.config)
        
        effective_mode = parsed.mode
        if args.matrix_mode:
            effective_mode = "matrix"

        if effective_mode == "matrix":
            targets = [] 
            labels = [] 
            for entry in args.matrix_mode.split(','):
                parts = entry.strip().split(':')
                if len(parts) >= 2:
                    label, sys_name, mode_val = parts[0], parts[1], (parts[2] if len(parts)>2 else "single")
                    targets.append(sys.name if hasattr(parts[1], 'name') else parts[1]) # Just use parts[1]
                    # Correcting logic to match target list expectation:
                    targets[-1] = parts[1]
                    labels.append(label)
                else:
                    targets.append(entry)
            
            output_file = orchestrator.run_matrix_mode(parsed.system, "matrix", parsed.tag, targets, parsed.extra_args)
        else:
            if not parsed.system:
                raise ValueError("--system is required when '--mode' is 'single'")
            output_file = orchestrator.run_single_mode(parsed.system, effective_mode, parsed.tag, parsed.extra_args)

        print(f"\n[SUCCESS] Report generation complete.")
        print(f"[INFO] Output file: {output_file}")

    except Exception as e:
        print(f"Execution Error: {e}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()