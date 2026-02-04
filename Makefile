setup:
	uv sync

test:
	uv run pytest

check:
	uvx ruff check .