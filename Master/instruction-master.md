## Master Startup CSV Aggregator

**Purpose:**  
Keep a single master CSV of all startups across every country folder in this workspace, with an extra `Country` column indicating which folder each entry came from, and **no duplicate startups by `Startup Name`**.

### What this folder contains

- `build_master_csv.py` – Python script that:
  - Recursively scans the workspace for **all `.csv` files** under the project root.
  - Skips the `Master` folder itself so it doesn't re-ingest the master CSV.
  - Infers a `Country` label from the **top-level folder name** under the root (e.g. `Indian Startups`, `UK Startups`, `US Startups`).
  - **Deduplicates** rows by `Startup Name` (case-insensitive, trimmed). First occurrence wins, later duplicates are skipped.
  - Writes/overwrites `master_startups.csv` in this folder.
  - Gracefully handles cases where some country folders don't have CSVs yet (e.g. no US/UK CSVs).

- `master_startups.csv` – Generated file containing:
  - All columns from the source CSVs.
  - An extra `Country` column with the name of the top-level folder the CSV came from.
  - At most one row per unique `Startup Name`.

### How to run this (for humans or AIs)

1. **Ensure you are in the workspace root** (the folder that contains `Indian Startups`, `UK Startups`, `US Startups`, and `Master`):

   ```bash
   cd "/Users/kshitij/Documents/cursor shit/clients from cursor"
   ```

2. **Run the aggregator script**:

   ```bash
   python3 "Master/build_master_csv.py"
   ```

3. After it finishes, open:

   ```bash
   Master/master_startups.csv
   ```

   to inspect the combined data.

### Notes for AI agents

- Treat `build_master_csv.py` as the **single source of truth** for building the master CSV.
- When new country folders or CSV files are added:
  - Do **not** hand-merge; just re-run the script from the workspace root.
- If you change the schema of the individual country CSVs:
  - The script already merges **all encountered columns** into the master header.
  - Make sure the per-country CSVs still have a `Startup Name` column so deduplication works.

