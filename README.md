# The Silver Logic Assignment

My first API using Django Rest Framework.

This project is online on Heroku: https://wall-app-tsl-api.herokuapp.com/

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

There's a `.env.example` file at `tsl` directory.

Rename to just `.env` and add the variables value

## Migrations

And then run migrations:
`python manage.py migrate`

## Run development server

Run `python manage.py runserver`

The server will be running at `http://127.0.0.1:8000/`

## Tests

To run the tests:
`python manage.py test`
