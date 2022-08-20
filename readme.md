# About

The repository contains code to scrape the load shedding schedule from [here](https://www.ke.com.pk/customer-services/load-shed-schedule/) and save it as a csv file. It makes use of KE's private api endpoint instead of running a headless browser setup which would be more resource intensive.

# Setup instructions

- Install Poetry package manager for Python

- Install all dependencies

- Switch to new virtual environment

- Execute the main script

## Linux/WSL

```
curl -sSL https://install.python-poetry.org | python3 -

poetry install

source "$(poetry env list --full-path | tail -1 | sed 's/.\{12\}$//')/bin/activate"

python __init__.py

```
