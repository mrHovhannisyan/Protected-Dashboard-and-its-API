# Dashboard-API

Backend application for Dashboard-Task.

An API service on python Flask framework.

# Local server

------------------------------------------------------------------------------------------------

## Requirements

------------------------------------------------------------------------------------------------

- [Python 3.8](https://www.python.org/downloads/) or higher


## Run on local machine

------------------------------------------------------------------------------------------------

### Make sure you’ve got Python & pip installed on your Local machine

Create a virtual environment*

```
virtualenv venv
```

_*You'll need `virtualenv` to be installed on your system_

```
pip install virtualenv
```

Activate virtualenv

```shell script
source venv/bin/activate
```

Install dependencies

```shell script
pip install -r requirments.txt
```

Copy the `.env.example` file to `.env` and change configuration to appropriate values

```shell script
cp .env.example .env
```

Run the migrations

```shell script
flask db upgrade
```

Start the application locally

```shell script
flask run
```

------------------------------------------------------------------------------------------------
### For running tests, simply type

```shell script
make test 
```


## Environment variables

| Variable                       | Description                                                   |
| -------------                  |:-------------:                                                |
| SECRET_KEY                     | A secret key that will be used for securely signing the session cookie and can be used for any other security related needs                        |
| SQLALCHEMY_DATABASE_URI        | Database connection URI.                                      |
