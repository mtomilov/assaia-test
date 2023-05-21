PHONY: *

lint:
	flake8 --max-line-length=88 connect
	mypy connect

test:
	pytest connect

upgrade-dev:
	pip-compile --output-file=requirements-dev.txt --resolver=backtracking requirements-dev.in

install-dev:
	pip-sync requirements-dev.txt
