.PHONY: env
env:
	poetry install

.PHONY: migrate
migrate:
	poetry run aerich upgrade

.PHONY: setup
setup:
	make env
	make migrate

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run pylint .
	poetry run pydocstyle .

.PHONY: run
run:
	poetry run python ./main.py
