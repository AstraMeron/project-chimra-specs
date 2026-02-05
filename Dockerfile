# Multi-stage Dockerfile for Project Chimera

# Stage 1: Builder - install tooling and create a virtualenv via `uv sync`
FROM python:3.13-slim AS builder
WORKDIR /app

# Install minimal build tools (if needed for pip installs)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is recent and install `uv` CLI used by the project
RUN python -m pip install --upgrade pip
RUN pip install uv

# Copy project metadata and run uv sync to populate .venv
COPY pyproject.toml pyproject.toml
RUN uv sync

# Stage 2: Runtime - copy the created virtualenv and application code
FROM python:3.13-slim AS runtime
WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder /app/.venv .venv

# Copy source code
COPY . .

# Ensure venv binaries are on PATH
ENV PATH="/app/.venv/bin:${PATH}"

# Default command: run tests when container executed without args
CMD ["uv", "run", "pytest"]
