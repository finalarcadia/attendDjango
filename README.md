# attendDjango
##Lates Notes
-Add cors dependency.
-Added instructions for clearing database, might need to with all the DB changes.
-
##Dependencies
```
sudo pip install Django
sudo pip install djangorestframework
sudo pip install django-cors-headers
```
##Database Clear
Terminal
```
rm -r /myapp/migrations
```
PSQL
```
DROP DATABASE attenddb;
```
Then create DB again with below instructions.
##Postgress

###1. Install homebrew

http://brew.sh/

###2. Terminal commands:
```
sudo brew install postgresql
sudo pip install psycopg2
```

###3. Run postgresql.app
http://postgresapp.com/

###4. Open psql (click elephant on top of screen)
psql commands:
```
CREATE DATABASE attenddb;
\connect attenddb
CREATE USER django WITH PASSWORD 'django' CREATEDB;
\q
```