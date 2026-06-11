# ReFrame Test Reporter

A modular Python tool for discovering, analyzing, and reporting eligible ReFrame tests by extracting structural metadata from `reframe --describe` JSON output.

---

## 🚀 Key Features

* **Single-System Reporting**: Generates comprehensive Markdown reports of eligible tests for a target system, complete with parameterized test breakdowns, descriptions, and organized test categories.
* **Dynamic Matrix Mode**: Automatically compares multiple test configurations or environment matrices, producing a cross-system test eligibility matrix (✅/❌) with summary metrics.
* **Parameter Breakdown**: Extracts internal ReFrame parameter injections (e.g., %param=val) and formats them into readable sub-bullets.
* **uenv Metadata Enrichment**: Extends ReFrame test listing by cross-checking:
  * `uenv image ls --json`
  * `reframe.yaml` from [https://github.com/eth-cscs/alps-uenv](https://github.com/eth-cscs/alps-uenv)


---

### 🔄 Workflow: Matrix Generation & uenv Integration

The reporter follows a multi-stage pipeline to transform raw ReFrame metadata and uenv environment information into a structured compliance matrix.

#### 1. Input Phase (Configuration)
* **CLI Arguments**: The user provides parameters such as `--matrix-mode` (defining targets), `--uenv-recipes-dir`, and `--uenv-image-inventory`.
* **Command Construction**: `CommandBuilder` parses these arguments and prepares the ReFrame command structure.

#### 2. Enrichment Phase (Environment Injection)
* **uenv Integration**: Before execution, the `Orchestrator` injects uenv paths into the subprocess environment:
    * `RFM_UENV_RECIPES_DIR` $\leftarrow$ `--uenv-recipes-dir` (ingests `reframe.yaml` data from the uenv recipes directory)
    * `RFM_UENV_IMAGE_INVENTORY` $\leftarrow$ `--uenv-image-inventory` (ingests output from `uenv image ls --json`)
* This ensures that ReFrame's `--describe` output is contextually aware of the available software recipes.

#### 3. Execution & Extraction Phase (ReFrame)
* **Subprocess Execution**: The `Executor` runs `reframe --describe` for each target in the matrix.
* **JSON Parsing**: The tool intercepts the standard output, isolates the JSON array within specific delimiters, and parses it into structured Python objects.

#### 4. Aggregation & Rendering Phase (Reporting)
* **Data Normalization**: Extracted metadata is normalized into a consistent schema.
* **Matrix Comparison**: For matrix mode, the `MatrixModeRenderer` compares the presence of tests across different targets.
* **Final Output**: A Markdown report is generated, featuring:
    * ✅/❌ eligibility checkboxes.
    * Parameter breakdowns (e.g., `%compiler=gcc`).
    * Organized test categories.

```mermaid
graph TD
    subgraph "Input Phase"
        A[CLI Arguments<br/>--matrix-mode, --uenv-*] --> B(CommandBuilder)
        C[uenv Recipes & Inventory] -.->|Injects Env Vars| B
    end

    subgraph "Execution Phase (ReFrame)"
        B --> D{Executor}
        D -->|Runs subprocess| E["reframe --describe<br/>(Target 1, Target 2, ...)"]
        E -->|Raw JSON Output| F[JSON Parser]
    end

    subgraph "Aggregation & Rendering"
        F --> G[Data Normalization]
        G --> H[MatrixModeRenderer]
        H --> I[Final Markdown Report<br/>with ✅/❌ Compliance]
    end
```
---

## 🛠️ Project Architecture

The core logic is structured cleanly within a decoupled, single-responsibility layout:

```text
reframe_reporter/
├── cli.py         # Parses CLI flags, applies defaults, and builds the configuration schema.
├── models.py      # Structured dataclasses ensuring internal type-safety (ReFrameReporterConfig).
├── builder.py     # Constructs sanitized ReFrame sub-commands and handles complex file naming logic.
├── executor.py    # Subprocess layer featuring bracket-isolation logic to pull clean JSON from noisy logs.
├── renderers.py   # Strategy-pattern generators translating parsed datasets into final Markdown tables.
└── utils.py       # Reusable, robust string sanitizers and Markdown-safe formatting helpers.
```

---

## 💻 Getting Started & Usage

Run the reporter using the main entry script (`run_report.py`).

### 1. Single-System Mode
Analyze a single target system configuration to list matching test profiles.
```bash
python3 run_report.py \
   --system daint \
   --mode production \
   -C cscs-reframe-tests/config/cscs.py \
   -c cscs-reframe-tests/checks
```

### 2. Matrix Mode (Multi-Target Coverage)
Provide multiple target entries to generate an aggregated test matrix. The `--matrix-mode` flag accepts a comma-separated list of targets formatted as `label:system:mode`.

**Example with multiple targets:**
```bash
python3 run_report.py \
   --matrix-mode "daint-maint:daint:maintenance,daint-prod:daint:production" \
   -C cscs-reframe-tests/config/cscs.py \
   -c cscs-reframe-tests/checks
```

### 3. Metadata Ingestion with User Environments (uenv)
Perform uenv-aware test listing using a previously generated uenv image inventory.

```bash
python3 run_report.py \
  --matrix-mode "daint-maint:daint:maintenance,daint-prod:daint:production" \
  --uenv-recipes-dir alps-uenv/recipes \
  --uenv-image-inventory alps-uenv/inventory.json \
  -C cscs-reframe-tests/config/cscs.py
```
* **Requirements** 
  * Creation of a uenv inventory (list of available uenvs on each vCluster)
    * See instructions below for generating uenv inventories
  * uenv recipes (from [alps-uenv](https://github.com/eth-cscs/alps-uenv))
---

## 📋 Command-Line Interface Reference

| Argument / Flag | Input Type | Description |
| :--- | :--- | :--- |
| `--system`           | `str`  | **Required for single-system runs.** Name of the target system (e.g., `daint`, `alps`). |
| `--mode`             | `str`  | CLI flag forwarded to ReFrame (e.g., `maintenance`, `production`). |
| `-C`, `--checks`     | `path` | **Required.** Directory containing ReFrame *check* files. Can be specified multiple times. |
| `-c`, `--config_dir` | `path` | **Required.** Directory containing *system* configuration files passed directly to ReFrame. |
| `-R`, `--recursive`| *Flag* | Instructs the framework to search for check directories recursively. |
| `-f`, `--filename` | `str` | Custom base string for the output report (Defaults to `eligible_tests.md`). |
| `-o`, `--output_dir` | `path` | Override path for outputs (Defaults to the checking script's root directory). |
| `--uenv-recipes-dir`| `path` | Repository containing the `reframe.yaml` files. |
| `--uenv-image-inventory`| `path`| Path to the JSON file containing the inventory of uenvs. |
| `--matrix-mode` | `str` | Comma-separated list map for system testing targets (`label:system:mode`). |
| `--matrix-tag` | `str` | Matrix entry argument filter (`label:arg`). Can be passed multiple times. |
| `-v`, `--verbose` | *Flag* | Enables verbose logging output. |

> 💡 **Note:** Any arguments provided at the very end of your script invocation following a double-dash (`--`) are cleanly processed, normalized, and seamlessly forwarded right to the underlying ReFrame subprocess.

---

## Coverage Matrix Snapshots

* [https://github.com/eth-cscs/cscs-reframe-tests/reframe_reporter/snapshots](./snapshots)

---

## How to Generate Coverage Reports 

### Prerequisite: Generate UENV inventories for the target systems

```bash
python3 ./cscs-reframe-tests/reframe_reporter/generate_uenv_image_inventory.py \
--output-dir  ./cscs-reframe-tests/reframe_reporter/snapshots/uenv-inventories/ \
--system daint,eiger,santis,clariden,starlex
```
### Single-System Report (Daint)

```bash
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--system daint --mode production \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/snapshots/uenv-inventories/uenv_image_inventory_daint.json \
-o cscs-reframe-tests/reframe_reporter/snapshots
```

### Coverage Matrix for Daint, Eiger, Santis, Clariden & Starlex

#### Maintenance 

```bash
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--matrix-mode daint-maint:daint:maintenance,eiger-maint:eiger:maintenance,santis-maint:santis:maintenance,clariden-maint:clariden:maintenance,starlex-maint:starlex:maintenance \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/snapshots/uenv-inventories/uenv_image_inventory_daint_eiger_santis_clariden_starlex.json \
-o cscs-reframe-tests/reframe_reporter/snapshots \
-f eligible_tests_matrix_mode-maintenance.md
```

#### Production 
```bash
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--matrix-mode daint-prod:daint:production,eiger-prod:eiger:production,santis-prod:santis:production,clariden-prod:clariden:production,starlex-prod:starlex:production \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/snapshots/uenv-inventories/uenv_image_inventory_daint_eiger_santis_clariden_starlex.json \
-o cscs-reframe-tests/reframe_reporter/snapshots \
-f eligible_tests_matrix_mode-production.md
```

#### Maintenance & Production

```bash
python3 cscs-reframe-tests/reframe_reporter/run_report.py \
--matrix-mode daint-maint:daint:maintenance,daint-prod:daint:production,eiger-maint:eiger:maintenance,eiger-prod:eiger:production,santis-maint:santis:maintenance,santis-prod:santis:production,clariden-maint:clariden:maintenance,clariden-prod:clariden:production,starlex-maint:starlex:maintenance,starlex-prod:starlex:production \
-C cscs-reframe-tests/config/cscs.py -c cscs-reframe-tests/checks \
-R --uenv-recipes-dir alps-uenv/recipes \
--uenv-image-inventory cscs-reframe-tests/reframe_reporter/snapshots/uenv-inventories/uenv_image_inventory_daint_eiger_santis_clariden_starlex.json \
-o cscs-reframe-tests/reframe_reporter/snapshots \
-f eligible_tests_matrix_mode-maintenance-production.md
```
