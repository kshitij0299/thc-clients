## Master Startup CSV Aggregator

**Purpose:**  
Keep a single **verified** master CSV of all startups across every country folder (rows must have **Founder LinkedIn URL** and/or **Founder Email**), with an extra `Country` column. No duplicate startups by `Startup Name`. At the end of every run, push the master CSV to the configured Google Sheet.

---

### What this folder contains

- **`build_master_csv.py`** – Builds the master CSV:
  - Recursively scans the workspace for **all `.csv` files** under the project root (skips the `Master` folder).
  - Infers **`Country`** from the top-level folder name (e.g. `Indian Startups`, `UK Startups`, `US Startups`).
  - **Deduplicates** by `Startup Name` (case-insensitive). First occurrence wins.
  - **Verified only:** includes only rows that have at least **Founder LinkedIn URL** or **Founder Email** (non-empty).
  - Writes/overwrites `master_startups.csv` in this folder.

- **`upload_to_sheets.py`** – Pushes the master CSV to Google Sheets:
  - Reads `master_startups.csv`, clears the configured worksheet, and writes all rows.
  - Requires `Master/service_account.json` (Google Cloud service account key). If missing, skips upload and prints a message.
  - Spreadsheet ID and worksheet name are set in the script (edit if you use a different sheet/tab).

- **`run_master_pipeline.py`** – Runs build then upload in one go. Use this for the full “every run” process.

- **`master_startups.csv`** – Generated file: all source columns + `Country`, one row per unique startup name, verified rows only.

---

### Full run (do this every time)

From the **workspace root** (the folder that contains `Indian Startups`, `UK Startups`, `US Startups`, and `Master`):

**Option A – one command (recommended):**

```bash
cd "/Users/kshitij/Documents/cursor shit/clients from cursor"
python3 "Master/run_master_pipeline.py"
```

This builds the verified master CSV, then runs the transfer to Google Sheet.

**Option B – run steps separately:**

```bash
cd "/Users/kshitij/Documents/cursor shit/clients from cursor"
python3 "Master/build_master_csv.py"
python3 "Master/upload_to_sheets.py"
```

**Automation:** Every run should include the transfer step so the Google Sheet is updated at the end. Use `run_master_pipeline.py` to do both in one go.

---

### Google Sheets setup (one-time)

1. **Google Cloud:** Create a project, enable **Google Sheets API**, create a **service account**, download its **JSON key**.
2. Save the key as `Master/service_account.json`.
3. **Share the target Google Sheet** with the service account email (Editor).  
   The script uses spreadsheet ID `1Q2QQiTK16zWFIenXn-Gpe3pHY54c6GikzsSXuAyWbrU` and worksheet `Sheet1` by default; edit `upload_to_sheets.py` if you use another sheet or tab.
4. Install deps once: `pip install gspread google-auth`

---

### Notes for AI agents

- **Single source of truth:** Use `build_master_csv.py` to build the master CSV; do not hand-merge.
- **Verified data:** Master CSV contains only rows with LinkedIn or email; the script filters automatically.
- **End of every run:** After building the master CSV, always run `upload_to_sheets.py` to complete the transfer to Google Sheets.
- If `service_account.json` is missing, the upload step is skipped (no error); the master CSV is still updated.
