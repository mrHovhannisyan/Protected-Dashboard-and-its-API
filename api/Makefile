.DEFAULT_GOAL:= help

.PHONY: test
test: ## Run tests
	venv/bin/python -m unittest discover

.PHONY: check
check: ## Check code with flake8
	venv/bin/python -m flake8

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
