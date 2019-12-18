# Cantera Song Lyrics Web Application  *Django*
**Web application with a list of songs with link to the lyrics, a calendar month by month with events. The admin site have three level access (superuser, Manager, Member). Superuser have all privileges. Member can add, update or delete song and event. Same for Manager who have also all privileges on Member.**

## Install
### Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
Connect to PostgreSQL client, create database and new user with privileges:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# CREATE USER "cantera";
postgres=# ALTER USER cantera WITH PASSWORD 'cool';
postgres=# CREATE DATABASE "db_cantera";
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_cantera TO cantera;
postgres=# \q
postgres@somewhere:~$ exit
```
### Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)):
```shell
$ git clone https://github.com/JBthePenguin/CanteraSongLyrics.git
$ cd CanteraSongLyrics
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
### Create tables
Make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
### Admin site
Create a "superuser" account:
```shell
(env)$ python manage.py createsuperuser
```
## Using
### Start the application
```shell
(env)$ python manage.py runserver
```
NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) for the admin site where you can add Manager, Member, Song and Event.
###### :metal: If you want access to the custom 'error 404' page, you have to set *DEBUG = False* in *settings.py line 26*, and run the server in insecure mode:
```python
DEBUG = False
```
```shell
(env)$ python manage.py runserver --insecure
```
