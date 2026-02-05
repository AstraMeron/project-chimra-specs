setup:
	uv sync

test:
	uv run pytest

check:
	uvx ruff check .

docker-build:
	docker build -t project-chimera-specs:latest .

docker-test:
	docker run --rm project-chimera-specs:latest uv run pytest