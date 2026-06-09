from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

@dataclass
class ReFrameReporterConfig:
    config_files: list[Path] = field(default_factory=list)
    check_paths: list[Path] = field(default_factory=list)
    recursive: bool = False
    uenv_recipes_dir: Optional[Path] = None
    uenv_image_inventory: Optional[Path] = None
    uenv_env: dict[str, str] = field(default_factory=dict)
    output_dir: Path = field(default_factory=lambda: Path.cwd())
    filename: str = "eligible_tests.md"
    system: str = ""
    mode: Optional[str] = None
    tag: Optional[str] = None

@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str
    cmd: list[str]
