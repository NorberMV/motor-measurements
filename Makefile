.PHONY: data test-reader

data:
	uv run python -m scripts.download_dataset

test-reader:
	uv run python -m scripts.test_reader