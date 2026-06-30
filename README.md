# Motor Temperature Analyzer

Python project for analyzing electric motor temperature sensor data (kaggle dataset).

## Setup

```bash
uv sync
```

## Get the data (~300 MB)

The raw dataset is **not committed** to git.

```bash
make data
# or
uv run python -m scripts.download_dataset
```

This uses `kagglehub` to download `wkirgsn/electric-motor-temperature` and places `data/measures.csv`.

### Kaggle auth

Either:
- `KAGGLE_API_TOKEN` in `.env`, or
- standard `~/.kaggle/kaggle.json`

## Run

```bash
make test-reader
# or
uv run python -m scripts.test_reader

# CLI example (uses data/measures.csv by default)
uv run python -m src.motor_temperature_analyzer.presentation.cli.main analyze-high-temp

# API
uv run uvicorn src.motor_temperature_analyzer.presentation.api.main:app --reload
```

## Environment override

Point at a different CSV without code changes:

```bash
export MOTOR_DATA_CSV=/path/to/your/measures.csv
```

## Notes

- `data/` and `*.csv` are gitignored.
- The project uses a src layout + setuptools build backend (editable install via `uv sync`).
- `uv run` is the recommended way to execute everything.
