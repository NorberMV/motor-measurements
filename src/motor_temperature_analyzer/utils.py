from pathlib import Path


csv_path = Path(__file__).resolve().parent.parent.parent / "data" / "measures.csv"


def get_csv_path():
    return csv_path