# Changelog

All notable changes to `list_tests.py` are documented here.

---

## [1.2.0] - 2026-06-02

### Added
- Added exact deployment mapping for local UENV recipes using `alps-uenv/config.yaml`.
- Local UENV recipe mode now assigns `target_systems` only for systems explicitly declared in `config.yaml`.

### Changed
- Switched local UENV recipe discovery from generic global availability to explicit system mapping.

---

## [1.1.1] - 2026-06-02

### Added
- Added `--uenv-recipes-dir` option to list UENV-enabled tests from local recipe metadata without installed uenv images.
- Local recipe mode is enabled by setting `RFM_UENV_RECIPES_DIR` for ReFrame subprocesses.

---

## [1.1.0] - 2026-05-30

### Changed
- Swapped fragile `reframe -L` textual/regex stdout parsing for native `reframe --describe` JSON serialization.
- Replaced custom stateful line matching with robust `json.loads()` processing, successfully addressing edge cases involving cropped or multi-line wrapped descriptions.
- Removed obsolete `--list-type` and `--exclude-related` CLI options since `--describe` strictly lists selected checks natively without tree entities.

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
- Reuse ReFrame’s selection logic instead of reimplementing filtering
- Retrieve test data using ReFrame's JSON output from --describe
