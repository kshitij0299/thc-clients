import csv
import os
from pathlib import Path


def find_source_csv_files(root: Path, master_dir_name: str = "Master") -> list[Path]:
    csv_files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip the master folder itself
        parts = Path(dirpath).parts
        if parts and parts[-1] == master_dir_name:
            continue

        for filename in filenames:
            if filename.lower().endswith(".csv"):
                csv_files.append(Path(dirpath) / filename)
    return csv_files


def infer_country_from_path(root: Path, file_path: Path) -> str:
    """
    Derive the 'country' label from the top-level folder under root.
    For example:
    - root / 'Indian Startups' / 'india-12_March_26.csv' -> 'Indian Startups'
    """
    rel = file_path.relative_to(root)
    parts = rel.parts
    if len(parts) == 1:
        # CSV directly under root – just label as 'root'
        return "root"
    return parts[0]


def build_master_csv() -> None:
    script_path = Path(__file__).resolve()
    master_dir = script_path.parent
    root = master_dir.parent

    source_csv_files = find_source_csv_files(root)

    if not source_csv_files:
        print("No source CSV files found. Nothing to do.")
        return

    master_csv_path = master_dir / "master_startups.csv"

    all_rows: list[dict[str, str]] = []
    master_fieldnames: list[str] | None = None
    seen_startup_names: set[str] = set()

    for csv_path in source_csv_files:
        country = infer_country_from_path(root, csv_path)

        with csv_path.open(mode="r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)

            # Initialize master fieldnames from the first CSV we see
            if master_fieldnames is None:
                master_fieldnames = list(reader.fieldnames or [])
                if "Country" not in master_fieldnames:
                    master_fieldnames.append("Country")
            else:
                # Union in any new fields that appear in later CSVs
                for field in reader.fieldnames or []:
                    if field not in master_fieldnames:
                        master_fieldnames.append(field)
                if "Country" not in master_fieldnames:
                    master_fieldnames.append("Country")

            for row in reader:
                # Normalize startup name for deduplication
                name = (row.get("Startup Name") or "").strip()
                key = name.lower()

                if not name:
                    # If there's no startup name, just skip dedupe and keep the row
                    # but still add the country
                    pass
                else:
                    if key in seen_startup_names:
                        continue
                    seen_startup_names.add(key)

                # Ensure all known master fields exist on the row
                normalized_row: dict[str, str] = {}
                for field in master_fieldnames:
                    if field == "Country":
                        normalized_row[field] = country
                    else:
                        normalized_row[field] = row.get(field, "") if row is not None else ""

                all_rows.append(normalized_row)

    if not all_rows or master_fieldnames is None:
        print("No rows collected from source CSVs.")
        return

    with master_csv_path.open(mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=master_fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)

    print(f"Master CSV written to: {master_csv_path}")


if __name__ == "__main__":
    build_master_csv()

