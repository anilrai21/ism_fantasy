# Magnificence

It is a sample project test project done for ISM tech test.  It is an api that returns a team of 7 football players with the most magnificence. 

## Things Used
1. Python3.12
2. Virtualenv
3. Sqlite
4. Makefile
   1. Make is usually installed by default on OSX and Linux.  So make commands can be used for installation
5. Django-ninja
6. Ruff


## Getting Started

1. Create Virtualenv 

    Run the command `virtualenv -p 3.12 venv` or `make create-venv`

2. Activate Virtualenv
    
    Run the command `source venv/bin/activate`

3. Install Dependencies

    Run the command `pip3 install -r requirements.txt` or `make install-dependencies`

4. Run Database migrations

    Run the command `python3 manage.py migrate` or `make migrate`

5. Populate the Database with data from API
   
    Run the command `python3 manage.py populate_data` or `make populate-data`

6. Start Django on local server
    
    Run the command `python3 manage.py runserver 0.0.0.0:8000` or `make runserver`

7. Run command to get the API.  It can be done in [API docs](http://localhost:8000/api/docs) or try to run the command using curl

    `curl http://localhost:8000/api/data/magnificent-team`


## Additional Steps

Run the tests for 
    
`python3 manage.py test` or `make test`

Run lint for the project

`ruff check` or `make lint`

Django has [admin page](http://localhost:8000/admin/) that can be accessed with a superuser.  Create a superuser and 

`python3 manage.py createsuperuser` or `make createsuperuser`

## Notes on my choices

I noticed that the input API data changes from time to time.  The limitation of the project is that population doesn't update the fields.

I have changed the magnificence calculation for Goalkeepers.  Since they don't score, I have changed it to use `saves` and `assists`

I have not added `magnificence` in the API as I only needed it for calculation.  It can be easily added by changing the schema for `Element` in Django-Ninja.

I have only created tables and fields that I assumed were required for rendering [this page](https://fantasy.premierleague.com/team-of-the-week/) as provided by on the brief.  It requires at least the following - 

1. The `web_name` for the player that is displayed
2. The `total_points` that is displayed with the name
3. The `chance_of_playing_this_round` and `chance_of_playing_this_round` to display the percentage on chance the player will play
4. The player `team` information for the team jersey design
5. The player `element_type` to place the player in the correct horizontal axis

I have kept a few more fields as they might just be useful.  I have limited the fields for the pitch view in the page.  List view will need more fields which can be easily added.

## Potential ideas if this is going to Production

1. Add logging for visibility that will show the bottlenecks for further improvements
2. Depending on the bottleneck - if this is going to be called a lot and the values will stay same for some time then caching can reduce load on the resources
3. Depending on the requirements of the Front end page, more fields can be added as I have limited myself as explained earlier.
4. Use `update_or_create` in when populating data as it changes quite frequently
