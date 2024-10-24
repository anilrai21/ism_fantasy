runserver:
	 python3 manage.py runserver 0.0.0.0:8000

populate-data:
	python3 manage.py populate_data

delete-all:
	python3 manage.py delete_all

lint:
	ruff format

lint-check:
	ruff check

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

test:
	python3 manage.py test

shell:
	python3 manage.py shell

create-venv:
	virtualenv -p 3.12 venv

install-dependencies:
	pip3 install -r requirements.txt

activate:
	source venv/bin/activate
