"""
Single entry point: build verified master CSV.
Run from workspace root: python3 Master/run_master_pipeline.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    scripts_dir = ROOT / "Master"
    build = scripts_dir / "build_master_csv.py"

    if not build.exists():
        print(f"Missing script: {build}")
        sys.exit(1)

    result = subprocess.run([sys.executable, str(build)], cwd=str(ROOT))
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
