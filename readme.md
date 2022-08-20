# Setup instructions

- Install Poetry package manager for Python

- Install all dependencies

- Switch to new virtual environment

- Execute the main script

```
curl -sSL https://install.python-poetry.org | python3 -

poetry install

source "$(poetry env list --full-path | tail -1 | sed 's/.\{12\}$//')/bin/activate"

python __init__.py

```
