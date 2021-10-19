install:
	pip install --upgrade pip --user &&\
		pip install -r requirements.txt --user

lint:
	python -m pylint --disable=R,C,W1203,W0702 ./app.py

test:
	python -m pytest -vv --cov=app ./test_app.py

format:
	python -m black *.py

all: install lint test
