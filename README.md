# attendDjango
----Postgress setup
1.
Install homebrew
http://brew.sh/

2.
terminal commands:

brew install postgresql
pip install psycopg2

3.
run postgresql.app
http://postgresapp.com/

4.
open psql (click elephant on top of screen),
psql commands:

CREATE DATABASE attenddb;
\connect attenddb
CREATE USER django WITH PASSWORD 'django' CREATEDB;
\q

---Populate your local db

python manage.py migrate
