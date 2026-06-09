import re
import os

class StringUtils:
    @staticmethod
    def sanitize_for_filename(name: str) -> str:
        """Removes characters that are unsafe for filenames."""
        # Replace non-alphanumeric/dash/underscore with underscore
        return re.sub(r'[^\w\.\-]', '_', name)

    @staticmethod
    def truncate_template_part(name: str, max_length: int = 50) -> str:
        """Truncates a string part while preserving the core identifier."""
        if len(name) <= max_length:
            return name
        return name[:max_length] + "..."

    @staticmethod
    def truncate_filename_int(name: str, max_length: int = 100) -> str:
        """Truncates a filename while preserving the extension."""
        base, ext = os.path.splitext(name)
        if len(name) <= max_length:
            return name
        # Ensure we don't over-truncate and break the structure
        new_base_len = max_length - len(ext) - 3
        return base[:new_base_len] + "..." + ext if (new_base_len > 0) else base[:max_length]

    @staticmethod
    def split_name_and_params(test_name: str) -> tuple[str, list[str]]:
        """Splits a test name into the base name and its parameters."""
        # Assumes params are in parentheses like 'test_name(param1, param2)'
        match = re.search(r'^(.*?)\((.*)\)$', test_name)
        if match:
            base_name = match.group(1)
            params = [p.strip() for p in match.group(2).split(',') if p.strip()]
            return base_name, params
        return test_name, []

    @staticmethod
    def normalize_table_string(text: str) -> str:
        """Converts newlines to HTML <br> for Markdown table compatibility."""
        return text.replace("\n", "<br>")
