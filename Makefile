.clean-venv:
	rm -rf .venv

.venv:
	poetry config virtualenvs.create true --local
	poetry install --sync
	pre-commit install

init: .clean-venv .venv

lint:  ## Lint the code
	@bash scripts/lint.sh $(args)

test:  ## Test the code
	@bash scripts/test.sh $(args)

build:
	@bash scripts/build.sh $(args)
