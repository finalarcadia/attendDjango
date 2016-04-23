# attendDjango
##TODO
1.Add cors dependency to your machine.
2.Change something in db if its too bothersome for some queries.
3.Look at comments in views.py on how to create classviews, and start creating some that the client needs
..*Examples: Given a userPK, return all classes user is enrolled in. 
..*Given a userPK, return university PK. 
..*Given universityPK, return all classes in university.
##Latest Notes
1.Added instructions for clearing database, might need to with all the DB changes. Remember to create some superusers again afterwards.
2.Removed some fields and added comments all throughout models.py, renamed some things. The less info might increase amount of querries, but the focus right now is fast communication with the client (the client sends Primary Keys only, the server gives it back data).
##Dependencies
```
sudo pip install Django
sudo pip install djangorestframework
sudo pip install django-cors-headers
```
Also: Postgress. See below.
##Database Clear/Add
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