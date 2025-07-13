#/bin/bash

uv sync
# ruff and pytest will apply configs in pyproject.toml automatically
uv run ruff format
uv run ruff check --fix --show-fixes
uv run reorder-python-imports --py312-plus --application-directories=src:tests
uv run pytest -vv