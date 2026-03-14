## Master Startup CSV Aggregator

**Purpose:**  
Keep a single **verified** master CSV of all startups across every country folder (rows must have **Founder LinkedIn URL** and/or **Founder Email**), with an extra `Country` column. No duplicate startups by `Startup Name`.

---

### What this folder contains

- **`build_master_csv.py`** – Builds the master CSV:
  - Recursively scans the workspace for **all `.csv` files** under the project root (skips the `Master` folder).
  - Infers **`Country`** from the top-level folder name (e.g. `Indian Startups`, `UK Startups`, `US Startups`).
  - **Deduplicates** by `Startup Name` (case-insensitive). First occurrence wins.
  - **Verified only:** includes only rows that have at least **Founder LinkedIn URL** or **Founder Email** (non-empty).
  - Writes/overwrites `master_startups.csv` in this folder.

- **`run_master_pipeline.py`** – Runs `build_master_csv.py` (single entry point for “every run”).

- **`master_startups.csv`** – Generated file: all source columns + `Country`, one row per unique startup name, verified rows only.

---

### Full run (do this every time)

From the **workspace root** (the folder that contains `Indian Startups`, `UK Startups`, `US Startups`, and `Master`):

```bash
python3 "Master/build_master_csv.py"
```

Or:

```bash
python3 "Master/run_master_pipeline.py"
```

---

### Notes for AI agents

- **Single source of truth:** Use `build_master_csv.py` to build the master CSV; do not hand-merge.
- **Verified data:** Master CSV contains only rows with LinkedIn or email; the script filters automatically.
- Run the build **at the end of every automation run** so the master CSV is up to date.
