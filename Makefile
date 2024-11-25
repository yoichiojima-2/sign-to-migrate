ROOT = $(shell pwd)
PROJECTS = data-collection server-side explore cleansing
VENV = $(ROOT)/.venv

.PHONY: clean
clean:
	-rm poetry.lock
	-find . -name "__pycache__" -type d -print -exec rm -rf {} +
	-find . -name ".pytest_cache" -type d -print -exec rm -rf {} +
	-find . -name ".ruff_cache" -type d -print -exec rm -rf {} +
	-find . -name ".ipynb_checkpoints" -type d -print -exec rm -rf {} +
	-find . -name "*.ipynb" -print -exec jupyter nbconvert --clear-output {} \;

.PHONY: lint
lint:
	-isort .
	-ruff check --fix .
	-ruff format .

.PHONY: pre-commit
pre-commit: lint clean

.PHONY: venv
venv: .venv/.installed
.venv/.installed: 
	python -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install pytest dateutils
	@for project in $(PROJECTS); do \
		$(VENV)/bin/pip install -e $$project ;\
	done
	touch $(VENV)/.installed

.PHONY: test
test: venv
	@for project in $(PROJECTS); do \
		cd $$project && $(VENV)/bin/pytest -vvv -s ;\
	done
