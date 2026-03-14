THC Clients – Startup Funding Datasets
======================================

This repository contains research agents and datasets for funded startups, organized by geography. Each region has its own folder with:

- **AGENTS-\<Region\>.md**: Detailed brief for how the research agent should find, clean, and enrich data for that region.
- **enrichment_instructions-\<Region\>.md**: Step‑by‑step instructions for enriching company and founder data, hiring signals, and outreach priorities.
- **CSV files**: One or more UTF‑8 CSVs with one row per startup, ready for outreach workflows.

### Folder structure

- **Indian Startups/**
  - `AGENTS-India.md`
  - `enrichment_instructions-INDIA.md`
  - `*.csv` files such as `india-12_March_26.csv` containing Indian startups funded in 2026.
- **UK Startups/**
  - `AGENTS-UK.md`
  - `enrichment_instructions-UK.md`
  - `*.csv` files for UK startups funded in 2026.
- **US Startups/**
  - `AGENTS-US.md`
  - `enrichment_instructions-US.md`
  - `*.csv` files for US startups funded in 2026.
- **Master/**
  - Aggregated **verified** CSV (rows must have Founder LinkedIn URL and/or Founder Email) from all region CSVs, with a `Country` column and no duplicate startup names.
  - `build_master_csv.py` – builds `master_startups.csv` from all `*.csv` files under the repo (excluding Master).
  - `upload_to_sheets.py` – pushes `master_startups.csv` to the configured Google Sheet (requires `Master/service_account.json`).
  - `run_master_pipeline.py` – runs build then upload in one go. See `Master/instruction-master.md` for full run and Google setup.

### How to use this repo

- **To understand the research logic**: Start by reading the relevant `AGENTS-<Region>.md` file for the geography you care about.
- **To run or extend research**: Follow the corresponding `enrichment_instructions-<Region>.md` file and append new rows to that region’s CSVs.
- **To consume the data**: Load the CSVs into your analytics or outreach tooling (Sheets, Airtable, CRM, warehouse, etc.) and filter by stage, sector, or outreach priority as defined in the instructions.
- **To build and sync the master list**: From the repo root run `python3 Master/run_master_pipeline.py`. This builds the verified master CSV from all region CSVs, then uploads it to the configured Google Sheet. See `Master/instruction-master.md` for one-time Google Sheets setup.

