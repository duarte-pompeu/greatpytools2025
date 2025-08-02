#/bin/bash
set -e

# install/sync versions based on current pyproject.toml and uv.lock
uv sync

# formatting
# ruff will apply configs from pyproject.toml automatically
uv run ruff format
uv run reorder-python-imports --py312-plus --application-directories src:tests

# linting
# ruff will apply configs from pyproject.toml automatically
uv run ruff check --fix --show-fixes

# testing
# pytest will apply configs from pyproject.toml automatically
uv run pytest -vv
