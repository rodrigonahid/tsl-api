# The Silver Logic Assignment

An API built in Python, using Django Framework.
Features:

- Registration, login and logout
- The Wall Dashboard (Authed)
- The Wall Dashboard (As guest)

## Clone the project

`git clone https://github.com/rodrigonahid/tsl-api.git`

## Set Virtual Env

Go to the root folder (same directory as `manage.py`)

`python3 -m venv env` to create the environmnent

If you are on Windows: `venv\Scripts\activate`
if your are on MacOS or Linux: `source env/bin/activate`

After sourcing the venv, pip install the dependencies:
`pip install -r requirements.txt`

And then run migrations:
`python manage.py migrate`

## Run development server

Run `python manage.py runserver`

The server will be running at `http://127.0.0.1:8000/`

## Enviroment variables (.env)

There's a `.env.example` file at `tsl` directory.

Rename to just `.env` and add the variables value

## Tests

To run the tests:
`python manage.py test`
