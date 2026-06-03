# list_tests.py — README

## Purpose

`list_tests.py` generates GitHub/GitLab-friendly Markdown reports of the checks **selected by ReFrame itself**, by running `reframe --describe` and parsing its JSON output.

The script supports **two execution modes**:

1. **Single-system mode (original behavior)** → Lists all tests selected for a given system + mode/tag.

2. **Matrix mode** → Generates a **cross-system and cross-mode/tag matrix view**, allowing you to see where each test is eligible to run.

In both cases, the script **does not re-implement ReFrame’s selection logic**. It simply formats the already-filtered results from ReFrame.

---

## Why this matches ReFrame's output

ReFrame’s frontend works in phases: it **discovers** tests, then **filters** them (by system and any other criteria), then performs an action such as describing.

When specifying `--describe`, ReFrame prints a complete JSON representation of all details (including the file where each test is defined and full descriptions) for the **selected** tests.

---

## Output

Running the script produces output files **relative to the script directory** (that is, the directory containing `list_tests.py`) when `--output_dir` is not provided.

### Single-system mode

Produces:
1. `*.md` — formatted report  
2. `*.reframe.out` — raw ReFrame JSON output

---

### Matrix mode 

Produces:
- A Markdown report with:
  - Tables of checks grouped by category
  - Matrix view (✅ / ❌)
  - Summary table
  - Timestamp

---

## Usage examples

### Single-system mode

```bash
python list_tests.py -C /path/to/config.py -c /path/to/checks -R --system daint --mode maintenance
```

---

### Matrix mode

```bash
python3 list_tests.py \
   --matrix-mode daint-maint:daint:maintenance \
   --matrix-mode eiger-maint:eiger:maintenance \
   --matrix-mode santis-maint:santis:maintenance \
   --matrix-mode clariden-maint:clariden:maintenance \
   -C ../config/cscs.py -c ../checks -R
```

---

### UENV data sources

This project supports two UENV retrieval modes:

1. **Direct UENV CLI output on a target system** — using `uenv image find --json @<system>`, which avoids the CLI’s default local-system filtering.
2. **Pre-generated inventory JSON** — using `generate_uenv_image_inventory.py` to build a stable inventory file that can be reused across runs.

We do not rely on `config.yaml` for UENV system mapping because it is not reliable; instead, we use explicit system filters or inventory JSON.

### Local UENV recipe mode

If you need to list UENV-enabled tests without installed uenv images, use a local recipe tree. Example:

```bash
python3 list_tests.py \
  --uenv-recipes-dir /Users/perettig/cscs/testing/alps-uenv/recipes \
  -C ../config/cscs.py -c ../checks -R --system daint --tag uenv
```

This sets `RFM_UENV_RECIPES_DIR` for the ReFrame subprocess and loads UENV metadata from local `extra/reframe.yaml` files.

---

## Command-line reference

```
usage: list_tests.py [-h] [--system SYSTEM] [--mode MODE] [--tag TAG]
                     [-C CONFIG_FILES] [-c CHECK_PATHS] [-R]
                     [-f FILENAME] [-o OUTPUT_DIR] 
                     [--matrix-mode MATRIX_MODE] [--matrix-tag MATRIX_TAG]
                     ...

Generate Markdown report by parsing ReFrame `--describe` JSON output.

positional arguments:
  extra                 Extra args passed to ReFrame after '--'

options:
  -h, --help            show this help message and exit
  --system SYSTEM       ReFrame system name (e.g. daint)
  --mode MODE           ReFrame execution mode (passed through)
  --tag, --tags TAG     Tag expression to pass to ReFrame (optional)
  -C CONFIG_FILES       ReFrame config file (repeatable: -C a.py -C b.py)
  -c CHECK_PATHS        Check path(s) (repeatable, passed through)
  -R                    Pass -R to ReFrame
  -f, --filename FILENAME
                        Base output filename (suffixes added automatically).
  -o, --output_dir OUTPUT_DIR
                        Output directory for the report (default: script
                        directory).
  --uenv-recipes-dir UENV_RECIPES_DIR
                        Path to local UENV recipe metadata for listing
                        UENV tests without installed uenv images.
  --matrix-mode MATRIX_MODE
                        Matrix entry: label:system:mode
  --matrix-tag MATRIX_TAG
                        Matrix entry: label:system:tag
```

---

## Troubleshooting

### Tests missing in the output

- Ensure `-R` is used
- Check ReFrame output for warnings (tests might be skipped)

---
