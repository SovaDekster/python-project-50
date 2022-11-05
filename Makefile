install: # Для первого git clone
	poetry install

build: #  Сборка пакета
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstallation:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

check:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
