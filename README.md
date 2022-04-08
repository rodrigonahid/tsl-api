# The Silver Logic Assignment

My first API using Django Rest Framework.

This project is online on Heroku: https://wall-app-tsl-api.herokuapp.com/posts

## Routes

-Register User:  POST `/users/`
-Log in User: POST `/users/token/`
-Make new post: POST `/posts/`
- Get all posts: GET `/posts/`

## Clone the project

`git clone https://github.com/rodrigonahid/tsl-api.git`

Then

`cd tsl-api`

## Set Virtual Env

On the root folder (same directory as `manage.py`)

`python3 -m venv env` to create the environment

If you are on Windows: `env\Scripts\activate`
if your are on MacOS or Linux: `source env/bin/activate`

After sourcing the venv, pip install the dependencies:
`pip install -r requirements.txt`

## Environment variables (.env)

There's a `.env.example` file at `tsl` directory. (`cd tsl/`)

Rename to just `.env` and add the variables value

Then go back to the root directory (`cd ..`)

## Migrations

On the root directory, run migrations:

`python manage.py migrate`

## Run development server

Run `python manage.py runserver`

The server will be running at `http://127.0.0.1:8000/`

## Enable debbuging

When on development, make sure to set `DEBUG = True` on `/tsl/settings.py`

## Tests

To run the tests:
`python manage.py test`
