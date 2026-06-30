from pathlib import Path
import os


def get_csv_path() -> Path:
    """Return path to the motor measurements CSV.

    Respects MOTOR_DATA_CSV env var override for local flexibility.
    Default: repo_root/data/measures.csv
    """
    env = os.getenv("MOTOR_DATA_CSV")
    if env:
        return Path(env).expanduser().resolve()
    return (Path(__file__).resolve().parent.parent.parent / "data" / "measures.csv").resolve()