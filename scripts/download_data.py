import os
import sys
import subprocess
from pathlib import Path

COMP = "ai-x-data-supervised-pillar-spring-2025"  # Kaggle competition slug

def run(cmd: list[str]) -> None:
    print(" ".join(cmd))
    subprocess.check_call(cmd)

def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / "data"
    data_dir.mkdir(exist_ok=True)

    # Install kaggle if needed
    try:
        import kaggle  # noqa: F401
    except Exception:
        run([sys.executable, "-m", "pip", "install", "kaggle"])

    # Check token exists
    kaggle_json = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_json.exists():
        print(
            "\nMissing Kaggle API token.\n"
            "1) Kaggle -> Profile -> Account -> Create New API Token (downloads kaggle.json)\n"
            "2) Move it to ~/.kaggle/kaggle.json and chmod 600 it:\n"
            "   mkdir -p ~/.kaggle\n"
            "   mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json\n"
            "   chmod 600 ~/.kaggle/kaggle.json\n"
        )
        sys.exit(1)

    # Download + unzip
    zip_path = data_dir / f"{COMP}.zip"
    run(["kaggle", "competitions", "download", "-c", COMP, "-p", str(data_dir)])
    if zip_path.exists():
        run(["unzip", "-o", str(zip_path), "-d", str(data_dir)])

    print("\nDone. Files should now be in ./data (train.csv, test.csv, sample_submission.csv).")

if __name__ == "__main__":
    main()
