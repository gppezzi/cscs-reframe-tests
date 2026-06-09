import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict

from .utils import StringUtils

class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data: List[Dict[str, Any]], path: Path, context: Dict[str, Any]):
        pass

    def normalize_table_string(self, text: str) -> str:
        return StringUtils.normalize_table_string(text)

    def split_name_and_params(self, test_name: str) -> tuple:
        from typing import Tuple
        res = StringUtils.split_name_and_params(test_name)
        return res

class SingleModeRenderer(ReportGenerator):
    def generate(self, data: List[Dict[str, Any]], path: Path, context: Dict[str, Any]) -> None:
        import datetime
        from urllib.parse import quote
        import re

        system = context.get("system", "unknown")
        mode = context.get("mode", "")
        tag = context.get("tag", "")
        found = len(data)

        ts = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
        
        content = [
            f"## Eligible ReFrame Tests on {system}",
            "",
            "- Filters:",
            f"  - system: `{system}`"
        ]
        if mode:
            content.append(f"  - mode: `{mode}`")
        if tag:
            content.append(f"  - tags: `{tag}`")
        content.append(f"  - checks: `{found}`")
        content.append(f"- Generated: `{ts}`")
        content.append("")
        content.append("| Test name | Description | Category |")
        content.append("|----------|-------------|----------|")

        def get_rel_path(f_path):
            if not f_path:
                return None
            norm = f_path.replace("\\", "/")
            if "/checks/" in norm:
                return "checks/" + norm.split("/checks/")[-1]
            if "checks/" in norm:
                return "checks/" + norm.split("checks/")[-1]
            return None

        def get_category(rel_path):
            if not rel_path:
                return "—"
            parts = rel_path.split("/")
            if len(parts) < 2 or parts[0] != "checks":
                return "—"
            folders = parts[1:-1]
            return "/".join(folders) if folders else "—"

        for test in data:
            display_name = test.get("display_name", "Unknown")
            file_path = test.get("file", "")
            description = test.get("description", "—")
            if not description:
                description = "—"
            
            # Formatting Test Name and Params
            base = re.sub(r"\s*%.*?(?=\s%|$)", "", display_name).strip()
            if not base:
                base = display_name
            params = re.findall(r"%.*?(?=\s%|$)", display_name)
            
            rel_path = get_rel_path(file_path)
            
            test_link_text = self.normalize_table_string(base)
            if rel_path:
                href = quote(f"../{rel_path}", safe="/._-")
                test_name_cell = f"[{test_link_text}]({href})"
            else:
                test_name_cell = test_link_text
                
            if params:
                bullets = "".join(f"<br>• {self.normalize_table_string(p)}" for p in params)
                test_name_cell += bullets

            # Formatting Category
            cat = get_category(rel_path)
            if cat and cat != "—":
                cat_href = quote(f"../checks/{cat}/", safe="/._-")
                cat_cell = f"[{self.normalize_table_string(cat)}]({cat_href})"
            else:
                cat_cell = "—"

            desc_cell = self.normalize_table_string(description)
            
            content.append(f"| {test_name_cell} | {desc_cell} | {cat_cell} |")

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))

class MatrixModeRenderer(ReportGenerator):
    def generate(self, data: List[Dict[str, Any]], path: Path, context: Dict[str, Any]) -> None:
        import datetime
        import re
        from urllib.parse import quote
        from collections import defaultdict
        
        timestamp = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
        content = ["## Test Coverage Matrix", "", f"- Generated: `{timestamp}`", ""]

        targets = context.get("targets", [])
        if not targets:
            return
            
        labels = [t + "-maint" for t in targets]
        grouped_tests = defaultdict(list)
        target_counts = {t: 0 for t in targets}

        existence_lookup = {}
        unique_tests = {}
        for test in data:
            display_name = test.get("display_name", "Unknown")
            file_path = test.get("file", "")
            target = test.get("target")
            
            key = (display_name, file_path, target)
            existence_lookup[key] = True
            
            if (display_name, file_path) not in unique_tests:
                unique_tests[(display_name, file_path)] = test

        for test in unique_tests.values():
            file_path_str = test.get("file", "")
            group_key = "other"
            
            rel_path = None
            if "/checks/" in file_path_str:
                rel_path = "checks/" + file_path_str.split("/checks/")[-1]
            elif "checks/" in file_path_str:
                rel_path = "checks/" + file_path_str.split("checks/")[-1]

            if rel_path:
                parts = rel_path.split("/")
                if len(parts) >= 2 and parts[0] == "checks":
                    folders = parts[1:-1]
                    if folders:
                        group_key = "/".join(folders)

            grouped_tests[group_key].append(test)
            
        sorted_groups = sorted(grouped_tests.keys())

        for group in sorted_groups:
            if group == "other" and not grouped_tests[group]:
                continue
            tests = grouped_tests[group]
            content.append(f"### {group}")
            content.append("") 
            
            header = ["Test name"] + labels
            sep_str = "|" + ("-----------|" * len(header))
            content.append("| " + " | ".join(header) + " |")
            content.append(sep_str)

            for test in sorted(tests, key=lambda x: (x.get("display_name", ""), x.get("file", ""))):
                display_name = test.get("display_name", "Unknown")
                file_path = test.get("file", "")
                
                rel_link = file_path
                if "/checks/" in file_path:
                    rel_link = "../checks/" + file_path.split("/checks/")[-1]
                elif "checks/" in file_path:
                     rel_link = "../" + file_path.replace("checks/", "", 1)

                base = re.sub(r"\s*%.*?(?=\s%|$)", "", display_name).strip()
                if not base:
                    base = display_name
                params = re.findall(r"%.*?(?=\s%|$)", display_name)

                test_link_text = self.normalize_table_string(base)
                if rel_link:
                    href = quote(rel_link, safe="/._-")
                    formatted_name = f"[{test_link_text}]({href})"
                else:
                    formatted_name = test_link_text

                if params:
                    bullets = "".join(f"<br>• {self.normalize_table_string(p)}" for p in params)
                    formatted_name += bullets

                row_cells = [formatted_name]
                for target in targets:
                    exists = existence_lookup.get((display_name, file_path, target), False)
                    if exists:
                        target_counts[target] += 1
                    row_cells.append("✅" if exists else "❌")
                content.append("| " + " | ".join(row_cells) + " |")
            content.append("")

        if target_counts:
            content.append("### Summary")
            content.append("")
            summary_header = ["Metric"] + labels
            summary_sep = "|" + ("--------|" * len(summary_header))
            content.append("| " + " | ".join(summary_header) + " |")
            content.append(summary_sep)
            summary_row = ["TOTAL"] + [str(target_counts[t]) for t in targets]
            content.append("| " + " | ".join(summary_row) + " |")

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
