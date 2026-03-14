"""
Upload master_startups.csv to the configured Google Sheet.
Run after build_master_csv.py. Requires: pip install gspread google-auth
"""
import csv
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

# Paths / IDs
ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "Master" / "master_startups.csv"
SERVICE_ACCOUNT_FILE = ROOT / "Master" / "service_account.json"

SPREADSHEET_ID = "1Q2QQiTK16zWFIenXn-Gpe3pHY54c6GikzsSXuAyWbrU"
WORKSHEET_NAME = "Sheet1"  # change if your tab name is different

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def upload_csv_to_sheet() -> None:
    if not SERVICE_ACCOUNT_FILE.exists():
        print("Service account key not found at Master/service_account.json. Skipping upload.")
        return
    if not CSV_PATH.exists():
        print("master_startups.csv not found. Run build_master_csv.py first.")
        return

    creds = Credentials.from_service_account_file(
        str(SERVICE_ACCOUNT_FILE),
        scopes=SCOPES,
    )
    client = gspread.authorize(creds)

    sh = client.open_by_key(SPREADSHEET_ID)
    try:
        ws = sh.worksheet(WORKSHEET_NAME)
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=WORKSHEET_NAME, rows="1000", cols="20")

    with CSV_PATH.open("r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = list(reader)

    ws.clear()
    if data:
        ws.update("A1", data)

    print(f"Uploaded {len(data)} rows to Google Sheet: {SPREADSHEET_ID}")


if __name__ == "__main__":
    upload_csv_to_sheet()
