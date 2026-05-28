# list_tests.py — README

## Purpose

`list_tests.py` generates GitHub/GitLab-friendly Markdown reports of the checks **selected by ReFrame itself**, by running `reframe -L` (list-detailed) and parsing its output.

The script supports **two execution modes**:

1. **Single-system mode (original behavior)**  
   → Lists all tests selected for a given system + mode/tag.

2. **Matrix mode (new)**  
   → Generates a **cross-system and cross-mode/tag matrix view**, allowing you to see where each test is eligible to run.

In both cases, the script **does not re-implement ReFrame’s selection logic**. It simply formats the already-filtered results from ReFrame.

---

## Why this matches ReFrame's output

ReFrame’s frontend works in phases: it **discovers** tests, then **filters** them (by system and any other criteria), then performs an action such as listing.

When listing, `-L/--list-detailed` prints details (including the file where each test is defined) for the **selected** tests.

---

## Output

Running the script produces output files **relative to the current working directory** (that is, the directory from which you invoke `list_tests.py`) when `--output_dir` is not provided.

### Single-system mode

Produces:
1. `*.md` — formatted report  
2. `*.reframe.out` — raw ReFrame output

---

### Matrix mode (new)

Produces:
- A Markdown report with:
  - Category tables
  - Matrix view (✅ / ❌)
  - Summary table
  - Timestamp

---

## Usage

### Single-system mode

```bash
python list_tests.py   -C /path/to/config.py   -c /path/to/checks   -R   --system daint   --mode maintenance
```

---

### Matrix mode

```bash
python3 list_tests.py --matrix-mode daint-maint:daint:maintenance --matrix-mode eiger-maint:eiger:maintenance  --matrix-mode santis-maint:santis:maintenance --matrix-mode clariden-maint:clariden:maintenance -C ../config/cscs.py -c ../checks -R
```

---

## Matrix output

- One column per system/mode/tag
- ✅ = eligible
- ❌ = not eligible

Includes:

- Timestamp
- Summary table

---

## Troubleshooting

### Few tests in matrix

- Ensure `-R` is used

---

