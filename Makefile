## ----------------------------------------------------------------------------

## This file holds common commands used for working with the codebase.
## Let's go!
## ----------------------------------------------------------------------------
## Run `make help` for help.
## ----------------------------------------------------------------------

# Which shell to use
# ----------------------------------------------------------------------
SHELL=/bin/bash

# Variables
# ----------------------------------------------------------------------

PYTHON ?= python3
VIRTUAL_ENV ?= venv

# Meta tasks
# ----------------------------------------------------------------------
.PHONY: help

ALL: help

# Task to parse all tasks from this Makefile and show their help texts.
help: ## Show this help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Load .env file into environment variables
# ----------------------------------------------------------------------
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

# Development tasks
# ----------------------------------------------------------------------
venv: ## Create a virtual environment
	$(PYTHON) -m venv "$(VIRTUAL_ENV)"

.PHONY: install-dependencies-base install-dependencies-dev install-dependencies-ai install-dependencies compile-dependencies install-pip-tools

install-pip-tools: ## Install pip-tools
	$(PYTHON) -m pip install pip-tools

compile-dependencies: ## Compile all dependencies
	pip-compile --upgrade -o requirements/base.txt requirements/base.in
	pip-compile --upgrade -o requirements/dev.txt requirements/dev.in

install-dependencies-base:
	pip-sync requirements/base.txt requirements/dev.txt

.PHONY: dagster_ui

dagster_ui:
	dagster dev -f core/definitions.py

preprocessing_job:
	dagster job execute -f core/definitions.py -j preprocessing_job

training:
	dagster job execute -f core/definitions.py -j training_job
