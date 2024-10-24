# Magnificence

It is a sample project test project done for ISM tech test.  It is an api that returns a team of 7 football players with the most magnificence. 

## Things Used
1. Sqlite
2. Django-ninja
3. Makefile


## Getting Started

1. Create Virtualenv 

    Run the command `virtualenv -p 3.12 venv` or `make create-venv`

2. Activate Virtualenv
    
    Run the command `source venv/bin/activate`

3. Install Dependencies

    Run the command `pip3 install -r requirements.txt` or `make install-dependencies`

4. Start Django on local server
    
    Run the command `python3 manage.py runserver 0.0.0.0:8000` or `make runserver`

5. Run Database migrations

    Run the command `python3 manage.py makemigrations` or `make makemigrations`

    Run the command `python3 manage.py migrate` or `make migrate`

6. Populate the Database with data from API
   
    Run the command `python3 manage.py populate_data` or `make populate-data`

7. Run command to get the API.  It can be done in [API docs](http://localhost:8000/api/docs) or try to run the command using curl

    `curl http://localhost:8000/api/data/magnificent-team`


## Additional Steps

Run the tests for 
    
`python3 manage.py test` or `make test`
