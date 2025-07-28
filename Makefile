run:
	@streamlit run app/main.py

format:
	@black app

lint:
	@flake8 app tests

test:
	@pytest

install:
	@pip install -r requirements.txt

freeze:
	@pip freeze > requirements.txt
