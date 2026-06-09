import os
from pathlib import Path
from typing import List, Optional
from .models import ReFrameReporterConfig

class CommandBuilder:
    def __init__(self, config: ReFrameReporterConfig):
        self.config = config

    def build_reframe_cmd(self, system: str, mode: str, tag: str, extra_args: List[str]) -> List[str]:
        """Constructs the ReFrame command with all necessary flags and arguments."""
        # 1. Start with base command
        cmd = ["reframe"]
        
        # 2. Apply core requirements for reporting/describing
        cmd.append("--describe")

        # 3. Add recursive flag if configured in ReFrameReporterConfig
        if self.config.recursive:
            cmd.append("-R")

        # 4. Add system-specific configuration if provided
        if system:
            cmd.extend(["--system", system])

        # 4.5 Add execution mode if provided (not the internal orchestrator modes)
        if mode and mode not in ["single", "matrix"]:
            cmd.extend(["--mode", mode])

        # 5. Handle the tag specifically if it wasn't part of a pattern
        if tag and mode not in ["matrix", "tag"]:
             cmd.extend(["--tag", tag])

        # 6. Process and Clean Extra Arguments (Ported from list_tests.py)
        cleaned_extra = self._normalize_extra(extra_args)
        cmd.extend(cleaned_extra)

        return cmd

    def build_rel_reframe_cmd(self, system: str, mode: str, tag: str, extra_args: List[str], target: str) -> List[str]:
        """Special builder for matrix targets to append the specific target string."""
        base_cmd = self.build_reframe_cmd(system, mode, tag, extra_args)
        return base_cmd + ["--system", target]

    def build_output_filename(self, system: str, mode: str, tag: str) -> str:
        """Constructs a sanitized and truncated filename for the report following legacy standards.
        Format: [base_name]_[system]_mode-[mode]_tags-[tag].[ext]
        """
        from .utils import StringUtils
        from pathlib import Path

        if system == "matrix":
            return f"{Path(self.config.filename).stem}_matrix.md"

        # At this point, we are guaranteed to be in a single-run context.
        base_name = self.config.filename
        stem = Path(base_name).stem
        parts = [StringUtils.sanitize_for_filename(stem)]

        # 2. Add system part (guaranteed not to be 'matrix')
        if system:
            parts.append(StringUtils.sanitize_for_filename(system))

        # 3. Add mode part (prefixed with 'mode-')
        # We only add mode if it's a specific execution mode, excluding the orchestrator type 'single'.
        if mode and mode != "single":
            parts.append(f"mode-{StringUtils.sanitize_for_filename(mode)}")

        # 4. Add tags part (prefixed with 'tags-')
        if tag:
            parts.append(f"tags-{StringUtils.sanitize_for_filename(tag)}")

        # Combine all parts and append the original extension
        filename = "_".join(parts) + Path(base_name).suffix
        return filename

    def extract_tag_from_extra(self, extra_args: List[str]) -> Optional[str]:
        for i, arg in enumerate(extra_args):
            if arg.startswith("--tag="):
                return arg.split("=", 1)[1]
            elif arg in ("--tag", "--tags") and i + 1 < len(extra_args):
                return extra_args[i+1]
        return None

    def extract_param_from_extra(self, extra_args: List[str], flag: str) -> Optional[str]:
        for i, arg in enumerate(extra_args):
            if arg == flag and i + 1 < len(extra_args):
                return extra_args[i + 1]
            elif arg.startswith(f"{flag}="):
                return arg.split("=")[1]
        return None

    def _normalize_extra(self, extra_args: List[str]) -> List[str]:
        if not extra_args:
            return []
        cleaned = list(extra_args)
        if cleaned and cleaned[0] == "--":
            cleaned = cleaned[1:]
        final_args = []
        skip_next = False
        for i, arg in enumerate(cleaned):
            if skip_next:
                skip_next = False
                continue
            if arg.startswith("--tag=") or arg in ("--tag", "--tags"):
                skip_next = True
                continue
            final_args.append(arg)
        return final_args
