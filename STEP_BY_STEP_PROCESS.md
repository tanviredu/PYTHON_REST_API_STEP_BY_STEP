1) first things first we need to create the environment
    do what i say no question:
    run this command in the terminal

    => pip3 install virtualenv
    => virtualenv -p python3 venv

    now activate the environment

    => source venv/bin/activate

    you will see the environment is activated in the shell

2) install the Packages

    => pip3 install django==2.0
    => pip3 install djangorestframework
    => pip3 install django-seed
    => pip3 install django-filter
    => pip3 install django-markdown

3) this is very important step

    => pip3 freeze > requirement.txt

    [it will save the metadata of all the installed packages in this file for future use]


4) create the project
    =>django-admin startproject BLOG

   Go to the directory and run the server

    => cd BLOG
    => python3 manage.py runserver

5) create the app inside the project

    => python3 manage.py startapp blog

6) add the blog app to the projects INSTALLED_APPS

7) migrate the app
    => python3 manage.py migrate

8) Create the admin user for the app

    => python3 manage.py createsuperuser

9) we create a model for the blog
    go to the models.py in the app
    two table
    1) Author table
    2) Article table

    and it will be connected with foreign key

10) now make the migration and migrate

    => python3 manage.py makemigrations
    => python3 manage.py migrate

