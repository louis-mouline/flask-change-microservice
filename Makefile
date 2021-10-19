install:
	pip install --upgrade pip --user &&\
		pip install -r requirements.txt --user

lint:
	pylint --disable=R,C,W1203,W0702 ./app.py

test:
	python -m pytest -vv --cov=app ./test_app.py

all: install lint test
