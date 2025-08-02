How to setup great python projects (2025 update)
---

In 2023, I presented *Tools to setup great python projects* in PyCon Portugal, where I talked about the tools I used to setup my python projects, and how I configured them under a centralized setup. 2 years later, my philosophy hasn't changed a lot, but I'm using new tools which have significant advantages - at least significant enough to ~go to Carcavelos and catch some sun~ give a talk about it. This article explains the same topics, in written form.

For package management, I am now using `uv`. It makes it easy to manage your dependencies, and locks their versions (and their sub-dependencies) in a file, leading to very reliable deployments. It's also very fast and includes other goodies.

For formatting, I switched to `ruff` + `reorder-python-imports`. The former is nice because it's fast and also lints, with reasonable defaults. The later is more niche, but enforces *one import per line*, which can decrease conflicts in `git`.

For code linting, I'm staying with `ruff`. It supports hundreds of rules and allows for safe (and unsafe!) auto-fixes.

For tests, I'm keeping `pytest`. It's more ergonomic than the native `unittest` and includes extra goodies such as:
- fixtures: re-usable objects (but better than global variables)
- parameters: re-use test code for different inputs/outputs

And I centralize all these configurations in `pyproject.toml`. This is very important! This will guarantee that other systems interacting with them (scripts, CLIs, IDEs, CI/CDs) will always use the same configuration! This results in a pleasing developer experience: **flexible workflows, consistent results**.

I'm also sharing other resources you may find useful:
- [slides](https://docs.google.com/presentation/d/1hS-bk3oHlplpQmQMP0biF3PKijS8rZ39_I8thtyTbvg/edit?usp=sharing)
- stream recording
- VOD
- [repo with example](https://github.com//duarte-pompeu/greatpytools2025)

# Tools

## Package manager

The two main things I look for in a package manager are:
- **an easy way to manage dependencies**
- **a lock with all main and sub-dependencies** (1)

Some recent languages, like go and rust, come with a good package manager. But Python is older and didn't start so great on this front, so it's been a rocky road for me:

- **pip**: easy to pull packages, but hard to manage versions across different projects (on its own)
- **pip + venv + requirements.txt**: a bit of a hack to get the job done: works but devx (developer experience) isn't great (2)
- **poetry** (or pipenv/pdm/others): reasonable devx with a lock file, but doesn't help with versioning of Python itself (or didn't, back then)
- **poetry + pyenv + pipx**: a complex setup that gets the job done, but requires some learning on how/why to use it (3)
- **uv**: as reliable as above, but much faster and all in one

So far, I'm happy with uv, which also has a few other goodies:
- install packages directly from git (poetry and others are also able to)
- easier to manage machine learning packages (heard pytorch is actually installable with `uv`)
- can install packages in editable mode (useful for development, poetry and others are also able to)


(1) as Matt Rickard puts it: there is a [Spectrum of Reproducibility](https://mattrickard.com/spectrum-of-reproducibility). Even a docker image is not 100% reproducible! But `uv.lock` is a great step without much effort.

(2) dev experience issues, from the top of my head:
- need to run a weird script to activate the virtualenv
	- didn't ran the script or forgot `--requires-virtualenv`: enjoy our package globally installed now
	- no built in way to separate groups of packages, eg deployable vs development
	- no built in way to lock all sub-dependencies

(3): here's what I used every tool for:
- poetry: manage project dependencies across projects
- pyenv: manage python version across projects
- pipx: install python tools not pinned to projects, eg `pre-commit` or `poetry`

## Formatting

I love `black`'s slogan, inspired by Henry Ford: *any color you want, as long as it's black*. I really appreciated its (mostly) uncompromising philosophy: formats into a reasonable layout, that can be enforced consistently. Importantly: it's easy to setup setup and has good defaults.

The **consistency** is key for me: no longer different IDEs or devs formatting code differently and causing messy diffs: just configure a formatter, enforce it and enjoy this issue going away!

With this being said, I was using `ruff` as a linter and it gained the capability to also format, with a very similar results (inspired by `black`, actualy), so I made the switch and simplified my setup. It's also faster, so I'll take that as a win.

A bit more niche, but I also replaced `isort` with `reorder-python-imports`. `isort` also has a nice slogan: *isort so you don't have to*; it behaved reasonably well, but I was introduced to `reorder-python-imports` with the following premise: 1 import per line leads to fewer git conflicts. I was skeptic and found it weird, but I gave it a try - and it does indeed reduce the amount of conflicts related to imports! So I'm being pragmatic and embracing it, along with  `ruff` (4).

Results:
- reasonable layout
- consistent formatting
- less time spent formatting manually (or discussing it in reviews)

(4) recently I heard `ruff` can be configured in a similar fashion - I'm looking forward to try that!

## Example

Before:

```python
from typing import List
import math
from random import seed, sample
import statistics


from itertools import *
from random import *





def pick_random_elements(list: List[int] = [], how_many_elements: int = 1, seed_for_deterministic_output = 0, a_forgotten_flag: bool = False) -> List[int]:
    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)





if __name__ == "__main__":
    print(f"Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
```

Commands (assuming you have `src/` and `tests/`):

```shell
uv run ruff format
uv run reorder-python-imports --py312-plus --application-directories src:tests
```

Results:

```python
from typing import List
import math
from random import seed
from random import sample
import statistics


from itertools import *
from random import *


def pick_random_elements(
    list: List[int] = [],
    how_many_elements: int = 1,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> List[int]:
    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)


if __name__ == "__main__":
    print(f"Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
```

## Linting

According to [Wikipedia](https://en.wikipedia.org/wiki/Lint_(software)), a linter is a "static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs". You can get more complex checks with LLMs or online services, but I prefer to use simple local tools. (5)

In the past I used `flake8`, but `ruff` has implemented most of its rules (and more), so that's why I'm using it now.

Results:
- avoid basic errors
- learn more about Python
- configure from hundreds of rules
- save time with auto-fixing

(5) but you can always augment your setup with other tooling! In my experience:
- enforce static analysis that is more limited but right 99% of the time
- suggest extra analysis that is more advanced but also has more false positives

## Example

Before:

```python
from typing import List
import math
from random import seed
from random import sample
import statistics


from itertools import *
from random import *


def pick_random_elements(
    list: List[int] = [],
    how_many_elements: int = 1,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> List[int]:
    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)


if __name__ == "__main__":
    print(f"Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
```

With the commands:

```shell
uv run ruff check --fix --show-fixes
```

Detected the following issues:

```
Found 9 errors:
UP035 `typing.List` is deprecated, use `list` instead
F401 [*] `math` imported but unused
F401 [*] `statistics` imported but unused
F403 `from itertools import *` used; unable to detect undefined names
F403 `from random import *` used; unable to detect undefined names
UP006 [*] Use `list` instead of `List` for type annotation
B006 Do not use mutable data structures for argument defaults
UP006 [*] Use `list` instead of `List` for type annotation
F541 [*] f-string without any placeholders
[*] 5 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
```

After fixing (some automatically, others manually):

```python
from random import sample
from random import seed


def pick_random_elements(
    list: list[int] | None = None,
    how_many_elements: int = 1,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> list[int]:
    if list is None:
        list = []

    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)


if __name__ == "__main__":
    print("Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
```


## Tests

`pytest` is almost like `requests`: the standard lib has similar tools included, but these are much nicer to use. 

I'm also curious about `hypothesis`, but use it rarely. I'm a fan of the oracle pattern: if you need to refactor function `f`, keep it and introduce `f_new`. Why the extra step and not just replace? Well, `f` will be an *oracle*, showing what's the correct output for a given input (if it was well coded!), so you can compare `f_new` against it. If both functions always return the same outputs, it's likely the refactor is correct (or more precisely, unlikely the refactor is incorrect)! (7)

Results:
- ergonomic tests
- it allows re-usable objects via *fixtures* (which are nicer than globals)
- it allows for re-usable tests via *parameters* 
- (and much more advanced stuff that I'm not using!)

(6) However, the final code it actually generates is a thing from nightmares, as shown by Pablo in PyCon Portugal 2025 :D

(7) Here's a better explanation from Hillen Wayne: [Hypothesis Testing with Oracle Functions](https://www.hillelwayne.com/post/hypothesis-oracles/)

# Example

```python
def test_f():
	assert 1 == 1.0
```

Parameters are interesting to multiply your tests. This has some advantages over putting multiple asserts in single test:
- report shows exactly which one failed
- runs all of them

```python
import pytest

@pytest.parametrize(
	"input, output",
	[
		(-100, -200),
		(-1, -2),
		(-0.0001, -0.0002)
		(0, 0),
		(0.0001, 0.0002),
		(1, 2),
		(100, 200)
	]
)
def test double(input, output)
	assert input == output
```

You can also assign custom names to each parameter (see pytest docs).

Fixtures allow you to re-use complex objects without globals. You can also:
- chain initialization of objects depending on others
- define when to initialize them (default: per function; but allows per module, per session, etc.)

```python
import pytest

@pytest.fixture
def parent():
	return get_complex_obj()

@pytest.fixture
def child_a(parent):
	return get_complex_obj(parent, some_param)

@pytest.fixture
def child_b(parent):
	return get_complex_obj(parent, another_param)

def test_parent(parent):
	assert parent.foo() is None

def test_child_a(child_a):
	assert child_a.foo() is not None

def test_child_b(child_b):
	assert child_b.foo() > 0

```

# Centralized configurations

With so many tools, it's important to make them a breeze to configure and use across many systems: scripts, CLIs, IDEs, CI/CDs, and so on. If you work in a team, this means these tools will affect you and all your colleagues too! There's two possible outcomes:
- do it well: everyone will have a smooth experience and appreciate the setup
- do it wrong: inconsistencies and errors will make it more painful than helpful

So, my way to "do it well" is simple:
1. configure everything in `pyproject.toml`
2. optional: write a simple script to apply checks you want 
3. enjoy the consistency across systems: CLIs, IDEs, scripts and CI/CDs

How so?

1: by default, these tools will look into `pyproject.toml` for configurations. Configuring them there allows you to run these utilities easily, without any flag, but still have them work consistently with the expected rules

2: a script defines the checks that can be performed, and can be enforced by CI/CD. This  way, everyone is on the same page: if the fix CI/CD complains about issues, you can run your script locally and fix them. **If it's fixed locally, it's fixed in CI/CD**.

3: what's this consistency about? Let's consider an example with formatting :
- CLI: just run `ruff format`
- IDE: just configure it to use `ruff format`
- Script: just write the basic commands, eg `ruff format`
- CI/CD: just run the script, or code the simple commands

If you specified the rules in `pyproject.toml`, all the examples from above will behave exactly the same! This brings nice results:
- avoid different devs using different formatting
- avoid CI/CD enforcing different formatting rules than devs expect
- avoids drift in configurations (eg change in one place but not in another)

# Wrapping up

In short, I'm using: `uv`, `ruff`, `reorder-python-imports` and `pytest` to setup my Python projects for a better experience. All configurations are centralized in `pyproject.toml` so they are easily re-usable across CLIs, IDEs, scripts and CI/CD.

This provides a setup with:
- reproducible deployments
- consistent formatting
- helpful static checks
- ergonomic testing
- consistent configurations

This is not a solution to all software engineering problems, not even close - but I find it basically solves these problems, so you have fewer distractions from the more complex ones!

# Audience questions

Relevant questions from the audience and my answers, with extra context after reflecting them on a bit.

**What do you think about pre-commit?**

I think it's a reliable way to configure all your tests, and even allow different workflows:
- users can run it manually
- users can install it in their git hooks
- CI/CD can also run it manually to perform the same checks

However, I oppose the use of custom pre-commit hooks, such as [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit). They will use different versions (maybe configurations?), which can introduce versioning/configuration drift, degrading developer experience. 

My approach is to keep it simple and define `system` hooks, which just fires commands in your CLI, eg  `uv run ruff format`. This plays perfectly into the **centralized configuration** approach:
- uses the same version as defined by`uv` (in `uv.lock`)
- uses the same configurations as defined in `pyproject.toml

**What about documentation?**

Currently not using any tools for that. I think it's more useful for libraries, where many users are interacting with the interfaces without reading the internals, while I'm mostly developing applications, in small teams who are familiar with the code (and can read the docstrings from their IDE).

**What about type checking?**

I find it useful to write type hints and check them occasionally, but I usually don't enforce it
- early in the project: experimental code, not caring about types
- late in the project: too many errors to enforce

But I'm curious about some new type checkers such as `ty` and `pyrefly`.

(I'm cheating, I put that question myself in advance due to a question from 2023 :p)
