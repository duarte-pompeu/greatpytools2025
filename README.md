Repo with references for the talk: How to setup great python projects (2025 update).

Includes:
- cheatsheet (bottom of README)
- script to run all checks: [checks.sh](./scripts/setup.sh)
- script to setup a minimal project with these tools: [setup.sh](./scripts/setup.sh)

I'm not including the lock file because it can get stale, but it's usually a good idea to also version control it.

# Checks

Save them in a script, allowing your devs and CI/CD to run them consistently:

```shell
bash scripts/checks.sh
```

If you want to tweak them, always prefer setting flags in `project.toml` than in the script, which has a few advantages:
- script is simpler
- running manually is simpler
- other tools, such as IDEs, will also find these flags, eg when formatting

# Cheatsheet

## uv

```shell
# install
curl -LsSf https://astral.sh/uv/install.sh | sh

# initialize project
cd <project-folder>
uv init --python 3.13

# install packages (usually automatic)
uv sync

# add packages
uv add requests
uv add pytest --dev
# TODO: editable mode
# TODO: github packages

# update packages (and their sub-dependencies)
uv add requests --upgrade

# run your programs
uv run python src/main.py

# lock packages (usually automatic)
uv lock
uv export > requirements.txt
```

## ruff

If we define the configs for ruff in [pyproject.toml](./pyproject.toml), these commands will apply them automatically:

```shell
# format code
uv run ruff format

# lint with safe auto-fixes
uv run ruff check --fix --show-fixes
```

## reorder-python-imports

```shell
uv run reorder-python-imports --py312-plus --application-directories=src:tests
```

## pytest

If we define the configs for pytest in [pyproject.toml](./pyproject.toml), these commands will apply them automatically:

```shell
uv run pytest
```