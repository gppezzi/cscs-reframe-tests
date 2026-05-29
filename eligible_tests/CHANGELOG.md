# Changelog

---

## [1.0.0] - 2026-05-28

### Added
- Matrix mode for cross-system coverage visualization:
  - `--matrix-mode label:system:mode`
  - `--matrix-tag label:system:tag`
- Matrix tables grouped by category
- Eligibility matrix with ✅ / ❌ indicators
- Summary table with totals per column
- Timestamp in matrix report
- Explicit debug output showing full ReFrame commands

### Improved
- Clear separation of mode and tag selection in matrix CLI
- Markdown formatting for summary tables
- Output files generated relative to script location
- Reuse of helper utilities (links, categories, filenames)

### Fixed
- Ensured `-R` is correctly propagated for recursive discovery
- Fixed `-L` / `--list` CLI conflict
- Fixed malformed TOTAL row in Markdown output
- Resolved inconsistencies between matrix and single-system results

### Behavior
- Single-system mode remains fully backward compatible
- Matrix mode is opt-in via `--matrix-*`

---

## [0.9.0] - 2026-05-27

### Added
- Initial matrix prototype combining multiple system runs
- Basic ✅ / ❌ matrix output
- First implementation of category grouping

### Notes
- Used generic `--target` CLI (later replaced)
- Partial formatting differences with original script

---

## [< 0.9.0] - Initial versions

### Features
- Single-system Markdown report generation
- Parsing of `reframe -L` output
- Category-based grouping
- Clickable links to test files
- Support for `--system`, `--mode`, `--tag`
- Support for `-C`, `-c`, `-R`
- Raw `.reframe.out` output capture

### Design principle
- Reuse ReFrame’s check selection logic (instead of reimplementing filtering using ReFrame's API)
