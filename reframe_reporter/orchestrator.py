import os
from pathlib import Path
from typing import Dict, Any, List
from .models import ReFrameReporterConfig
from .builder import CommandBuilder
from .executor import ReFrameReporterExecutor
from .renderers import SingleModeRenderer, MatrixModeRenderer

class ReportOrchestrator:
    def __init__(self, config: ReFrameReporterConfig):
        self.config = config
        self.builder = CommandBuilder(config)
        self.executor = ReFrameReporterExecutor()
        self.single_renderer = SingleModeRenderer()
        self.matrix_renderer = MatrixModeRenderer()

    def _get_target_dir(self) -> Path:
        """Determines the target directory for output based on config."""
        if self.config.output_dir:
            return self.post_process_path(self.config.output_dir)
        elif self.config.check_paths:
            return self.config.check_paths[0].parent
        else:
            return Path(".")

    def post_process_path(self, path: Path) -> Path:
        """Ensures the output directory exists."""
        os.makedirs(path, exist_ok=True)
        return path

    def run_single_mode(self, system: str, mode: str, tag: str, extra_args: List[str]) -> Path:
        """Executes a single ReFrame command and generates a report."""
        cmd = self.builder.build_reframe_cmd(system, mode, tag, extra_args)
        env = self._prepare_env(system)
        print(f"Executing Single Mode: {' '.join(cmd)}")
        result = self._run_and_save_raw(cmd, env)

        if result.returncode != 0:
            self._report_failure("Single Mode", cmd, result)
            data = []
        else:
            try:
                data = self.executor.parse_json(result.stdout)
            except ValueError as e:
                print(f"ERROR: {e}")
                data = []

        filename = self.builder.build_output_filename(system, mode, tag if tag else "")
        target_dir = self._get_target_dir()
        output_path = target_dir / filename
        context = {
            "system": system, 
            "mode": mode, 
            "tag": tag,
            "checks_dir": str(self.config.check_paths[0] if self.config.check_paths else "")
        }
        self.single_renderer.generate(data, output_path, context)
        return output_path

    def run_matrix_mode(self, system: str, mode: str, tag: str, targets: List[str], extra_args: List[str]) -> Path:
        """Executes ReFrame for multiple targets and aggregates results."""
        all_results = []
        processed_targets_ordered = []
        any_failures = False

        for target in targets:
            clean_target = target.strip()
            label = clean_target.split(':')[0] if ':' in clean_target else clean_target
            exec_system = clean_target.split(':')[1] if ':' in clean_target else clean_target

            cmd = self.builder.build_rel_reframe_cmd(system, mode, tag, extra_args, exec_system)
            env = self._prepare_env(system)
            print(f"Executing Matrix Target: {exec_system} (Label entry: {label})")
            print(f"Executing Matrix Mode Command: {' '.join(cmd)}")
            result = self._run_and_save_raw(cmd, env)

            if result.returncode == 0:
                try:
                    data = self.executor.parse_json(result.stdout)
                    for item in data:
                        item["target"] = clean_target 
                        all_results.append(item)
                    if clean_target not in processed_targets_ordered:
                        processed_targets_ordered.append(clean_target)
                except ValueError as e:
                    print(f"ERROR: {e}")
                    any_failures = True
            else:
                self._report_failure(f"Matrix Target ({clean_target})", cmd, result)
                any_failures = True

        filename = self.builder.build_output_filename("matrix", mode, tag if tag else "")
        target_dir = self._get_target_dir()
        output_path = target_dir / filename
        context = {
            "system": system,
            "mode": mode,
            "tag": tag,
            "targets": processed_targets_ordered if processed_targets_ordered else targets,
            "any_failures": any_failures
        }
        self.matrix_renderer.generate(all_results, output_path, context)
        return output_path

    def _report_failure(self, context_label: str, cmd: List[str], result: Any) -> None:
        """Detailed error reporting for failed ReFrame executions."""
        print(f"\n{'!'*20} ERROR {'!'*20}")
        print(f"Context: {context_label}")
        print(f"Command: {' '.join(cmd)}")
        print(f"Return Code: {result.returncode}")
        if result.stdout:
            print(f"\n--- STDOUT --- \n{result.stdout}")
        if result.stderr:
            print(f"\n--- STDERR --- \n{result.stderr}")
        print(f"{'!'*49}\n")

    def _run_and_save_raw(self, cmd: List[str], env: Dict[str, str]) -> Any:
        """Executes the command and preserves raw stdout/stderr to a file."""
        result = self.executor.run(cmd, env=env)
        try:
            directory = self._get_target_dir()
            from .utils import StringUtils
            raw_name = "reframe_raw"
            raw_filename = StringUtils.sanitize_for_filename(raw_name) + ".reframe.out"
            raw_path = directory / raw_filename
            os.makedirs(directory, exist_ok=True)
            with open(raw_path, "w") as f:
                f.write("=== COMMAND ===\n")
                f.write(" ".join(cmd) + "\n")
        except (OSError, IOError) as e:
            print(f"WARNING: Failed to save raw output file due to I/O error: {e}")
        except Exception as e:
            print(f"WARNING: An unexpected error occurred while saving raw output: {e}")
        return result

    def _prepare_env(self, system: str) -> Dict[str, str]:
        """Prepares the environment variables."""
        env = os.environ.copy()
        if self.config.uenv_recipes_dir:
            env["RFM_UENV_RECIPES_DIR"] = str(self.config.uenv_recipes_dir.resolve())
        if self.config.uenv_image_inventory:
            env["RFM_UENV_IMAGE_INVENTORY"] = str(self.config.uenv_image_inventory.resolve())
        if self.config.uenv_recipes_dir or self.config.uenv_image_inventory:
            env["RFM_UEV_TARGET_SYSTEMS"] = system 
        env.update(self.config.uenv_env)
        return env
