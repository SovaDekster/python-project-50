install: # Для первого git clone
	poetry install

build: #  Сборка пакета
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff tests

check:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
