import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
import kagglehub


load_dotenv()
os.environ["KAGGLE_API_TOKEN"] = os.getenv("KAGGLE_API_TOKEN")

DATA_DIR = Path("data")
TARGET = DATA_DIR / "measures.csv"


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading dataset via kagglehub...")
    dl_path = Path(kagglehub.dataset_download("wkirgsn/electric-motor-temperature"))
    print(f"kagglehub cache: {dl_path}")

    # The actual file is measures_v2.csv inside the versioned folder
    candidates = list(dl_path.rglob("measures_v2.csv"))
    if not candidates:
        raise FileNotFoundError(f"measures_v2.csv not found under {dl_path}")

    src = candidates[0]
    print(f"Found source: {src}")

    if TARGET.exists():
        print(f"{TARGET} already exists, skipping (delete it to re-download).")
        return

    shutil.copy2(src, TARGET)
    size = TARGET.stat().st_size / (1024 * 1024)
    print(f"Copied to {TARGET} ({size:.1f} MB)")


if __name__ == "__main__":
    main()