Repo with references for the talk: How to setup great python projects (2025 update).

Includes:
- cheatsheet (bottom of README)
- script to run all checks: [checks.sh](./scripts/checks.sh)
- script to setup a minimal project with these tools: [setup.sh](./scripts/setup.sh)

Note: I'm not including the lock file in this repo because it can get stale, but it's usually a good idea to also version control it (except if you're working in a re-usable lib, where you may want users to have flexibility in versioning).

# Checks

Save them in a script, allowing your devs and CI/CD to run them consistently:

```shell
bash scripts/checks.sh
```

We can also use `pre-commit` instead of shell scripts. With pre-commit, I recommend that you use `language: system` and let `uv` manage your versioning and `pyproject.toml` your configs; otherwise, you'll duplicate your effort and risk drift in configs and versions. Then you can:

```shell
# run manually
uv tool run pre-commit run -a
# install as as a git hook (applies automatically when committing)
uv tool run pre-commit install
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

# run your programs
uv run python src/main.py

# add packages
uv add requests
uv add pytest --dev
# TODO: editable mode
# TODO: github packages

# update packages (and their sub-dependencies)
uv add requests --upgrade

# remove packages
uv remove requests

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
uv run reorder-python-imports --py312-plus --application-directories src:tests
```

## pytest

If we define the configs for pytest in [pyproject.toml](./pyproject.toml), these commands will apply them automatically:

```shell
uv run pytest
```
