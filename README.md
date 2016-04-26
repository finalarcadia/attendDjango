# attendDjango
##TODO
##Latest Notes
##Dependencies
```
sudo pip install Django
sudo pip install djangorestframework
sudo pip install django-cors-headers
sudo pip install django-filter
sudo pip install django-url-filter
```
Also: Postgress. See below.
##Database Clear/Add/Start
###Clear
terminal
```
rm -r myapp/migrations
```
psql
```
DROP DATABASE attenddb;
```
###Add
psql
```
CREATE DATABASE attenddb;
\connect attenddb
CREATE USER django WITH PASSWORD 'django' CREATEDB;
\q
```
###Start
```
python manage.py makemigrations myapp
python manage.py migrate
```
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
Click elephant (top of screen) to run psql
#The Holy Bible
https://docs.djangoproject.com/en/1.9/intro/tutorial01/
http://www.django-rest-framework.org/tutorial/quickstart/