install: # for first gitclone
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstallation:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
