How to setup great python projects (2025 update)
---

Reference code for the talk: How to setup great python projects (2025 update), by Duarte Pompeu. You may also be interested in:

- [slides](https://docs.google.com/presentation/d/1hS-bk3oHlplpQmQMP0biF3PKijS8rZ39_I8thtyTbvg/edit?usp=drivesdk) used in the talk
- [stream](https://youtu.be/gJf-SpCAN9w?t=8469) (unfortunately it has audio issues)
- [article](./article.md): the written version of the talk 
- VOD: soon?

Includes:
- cheatsheet (bottom of README)
- script to setup a minimal project with these tools: [setup.sh](./scripts/setup.sh)
- script to run all checks: [checks.sh](./scripts/checks.sh)


Note: I'm not including the lock file in this repo because it can get stale, but it's usually a good idea to also version control it (except if you're working in a re-usable lib, where you may want users to have flexibility in versioning).

# Configuration

I always recommend that you configure these tools in `pyproject.toml`. Tools will look into it by default, and this has nice advantages:
- reduces config drift
- running from the CLI is really simple, eg `uv run ruff check` will automatically apply all the rules

What usually happens when you don't centralize the configs:
- extra effort: need to specify configs in scripts, IDE, CI/CD, always type them when running in CLI
- config drif: if you want to change any configuration, and you forget to change it everywhere, it leads to drift and annoyances, eg CI/CD enforcing different rules than your local checks

# Checks

## Script

If you want to keep it simple, you can store the commands in a script, that can be used by devs and CI/CD.

```shell
bash scripts/checks.sh
```

## Pre-commit

You can also use `pre-commit` instead of shell scripts.
With pre-commit, I recommend that you always use `language: system` and let `uv` manage your tools, reducing duplicate efforts and configuration drifs.

```shell
# run manually
uvx pre-commit run -a
# install as as a git hook (applies automatically when committing)
uvx pre-commit install
```

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
uv run python hello.py

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

TODO: define files in pyproject.toml!

```shell
uv run reorder-python-imports --py312-plus --application-directories src:tests
```

## pytest

If we define the configs for pytest in [pyproject.toml](./pyproject.toml), these commands will apply them automatically:

```shell
uv run pytest
```
