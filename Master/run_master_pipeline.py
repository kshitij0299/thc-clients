"""
Single entry point: build verified master CSV, then upload to Google Sheet.
Run from workspace root: python3 Master/run_master_pipeline.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    scripts_dir = ROOT / "Master"
    build = scripts_dir / "build_master_csv.py"
    upload = scripts_dir / "upload_to_sheets.py"

    for script in (build, upload):
        if not script.exists():
            print(f"Missing script: {script}")
            sys.exit(1)

    result = subprocess.run([sys.executable, str(build)], cwd=str(ROOT))
    if result.returncode != 0:
        sys.exit(result.returncode)

    result = subprocess.run([sys.executable, str(upload)], cwd=str(ROOT))
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
