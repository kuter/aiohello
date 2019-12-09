development:
	pip install -r requirements/dev.txt
	pre-commit install

run:
	python app.py

test:
	pytest
