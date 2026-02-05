setup:
	uv sync

test:
	uv run pytest

setup:
	@echo "Creating virtual environment and installing minimal deps..."
	python -m venv .venv || true
	.venv\Scripts\pip install -r requirements.txt || true

spec-check:
	@python - <<'PY'
import sys,os
root = os.path.dirname(__file__)
needed = [
    os.path.join(root,'specs','_meta.md'),
    os.path.join(root,'specs','functional.md'),
    os.path.join(root,'specs','openclaw_integration.md'),
]
missing = [p for p in needed if not os.path.exists(p)]
if missing:
    print('Missing spec files:', missing)
    sys.exit(2)
print('Spec check passed')
PY

check:
	uvx ruff check .

docker-build:
	docker build -t project-chimera-specs:latest .

docker-test:
	docker run --rm project-chimera-specs:latest uv run pytest