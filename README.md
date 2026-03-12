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

### How to use this repo

- **To understand the research logic**: Start by reading the relevant `AGENTS-<Region>.md` file for the geography you care about.
- **To run or extend research**: Follow the corresponding `enrichment_instructions-<Region>.md` file and append new rows to that region’s CSVs.
- **To consume the data**: Load the CSVs into your analytics or outreach tooling (Sheets, Airtable, CRM, warehouse, etc.) and filter by stage, sector, or outreach priority as defined in the instructions.

