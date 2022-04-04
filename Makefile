
dist: deflines
	pip install build
	python -m build

.PHONY: install
install: dist
	pip install --force-reinstall dist/*.whl

.PHONY: allchecks
allchecks: stylecheck typecheck test smoketest

.PHONY: test
test:
	pytest -v .

.PHONY: smoketest
smoketest:
	PYTHONPATH=. python deflines/cli.py

.PHONY: stylefix
stylefix:
	isort --settings-path pyproject.toml .
	black --config pyproject.toml .

.PHONY: stylecheck
stylecheck:
	isort --settings-path pyproject.toml --check .
	black --config pyproject.toml --check .

.PHONY: typecheck
typecheck:
	mypy deflines/
