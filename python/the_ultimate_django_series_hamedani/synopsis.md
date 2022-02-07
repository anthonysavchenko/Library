# The Ultimate Django Series

*By Mosh Hamedani*


## References

[Source](https://codewithmosh.com/courses/1422300)

[Repository](https://github.com/anthonysavchenko/Storefront)


## Django fundamentals


### Start a New Project


1. Install latest Python version (https://python.org) and VSCode (https://code.visualstudio.com)

2. `pipenv install django` - install latest Django version

3. Create Django project using `django-admin` utility


### Command Line Utility - Create a New Django Project, etc

`dgango-admin` - command line utility to manage Django project

`dgango-admin startproject storefront` - create a new project

`dgango-admin startproject storefront .` - create a new project into the current directory (do not create project folder)

`py manage.py runserver` - run current project


### New Project Structure

`core directoy`

    `__init__.py` - defines directory as a package

    `settings.py` - application settings

    `urls.py` - application endpoints

    `asgi.py` and `wsgi.py` - used for deployment

`manage.py` - wrapper around `django-admin` wich takes into account project settings


### Apps

Default apps:

    `admin` - admin page

    `auth` - to authenticating users

    `contenttypes` - later

    `sessions` - legacy, may be deleted

    `messages` - to display notifications to the user

    `staticfiles` - to serving static files (images, CSS)

`py manage.py startapp playground` - create a new app

App structure:

    `migrations` - directory to store migrations

    `admin.py` - defines how admin interface for this app is look like

    `apps.py` - app configuration

    `models.py` - stores model classes

    `tests.py` - stores unit tests

    `views.py` - later (controllers)


## Building a Data Model

Unix philosophy: Do one thing and bo it well

Bad design: monolith, fine grained with a lot of coupling

Good design: minimal coupling, high cohesion (focus on specific functionslity)


## Setting Up the Database

`py manage.py makemigrations` - generate migration files

`py manage.py migrate` - run migration files

`py manage.py sqlmigrate store 0003` - show SQL-code for third migration of store app

**sequel** - structured english query language

`py manage.py migrate store 0004` - revert migrations after third migration of store app

`py manage.py migrate store --empty` - create empty migration to add some custom SQL into migration

https://mockaroo.com - generates fake (dummy) data


## Django ORM

ORM - object-relational mapper.

### Classes

Expression
    - Value
    - F
    - Func
    - Aggregate
    - ExpressionWrapper


## The Admin Site

