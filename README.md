# Attend.io Backend

Django and Django REST Framework For Attend.io

![api root](/screenshots/home.png)

#Usage

### Python Virtual Machine (Unix)

1. `source venv/bin/activate` - Load the environment, run scripts and develop under environment
2. `deactivate` - Unload the environment when you're done with python

### Django Quickstart

* `python manage.py createsuperuser` - add yourself to the database as an admin so that you can login to the REST API
* `python manage.py migrate` - apply model changes
* `python manage.py runserver` - run test server default is http://localhost:8000

###Database reset & restart
####Reset
terminal
```
rm -r myapp/migrations
```
psql
```
DROP DATABASE attenddb;
```
####Restart
```
python manage.py makemigrations myapp
python manage.py migrate
```


# Installation

##Postgress

First you must install the database.

###1. Install homebrew (Mac)

http://brew.sh/

###2. Install postgresql (Mac):
```
brew install postgresql
brew services start postgresql
```

###3. Set up database:
psql
```
CREATE DATABASE attenddb;
\connect attenddb
CREATE USER django WITH PASSWORD 'django' CREATEDB;
\q
```

### Python Virtual Environment

This project is best ran in a virtual environment. You can use [pyvenv][2],
which comes with python 3 and greater. The virtual enviroment lets you run
different versions of python and packages from other projects.

#### Django Installation (Unix)

First install python2+ on your machine and then download and install [pip][1].
Then from the root of the project run:

1. `pyvenv venv` - Create a virtual environment in the venv folder
2. `source venv/bin/activate` - Load the environment
3. `pip install -r Requirements.txt` - Install dependencies
4. `deactivate` - Unloads the environment