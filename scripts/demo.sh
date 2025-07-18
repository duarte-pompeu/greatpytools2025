uv run reorder-python-imports --py312-plus --application-directories src/*formatting*.py
uv run ruff format src/*formatting*.py

uv run ruff check src/with_formatting_plus_linting.py --fix

uv run pytest