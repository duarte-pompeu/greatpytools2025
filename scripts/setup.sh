curl -LsSf https://astral.sh/uv/install.sh | sh
uv init --python 3.13
uv add --dev ruff reorder-python-imports pytest
