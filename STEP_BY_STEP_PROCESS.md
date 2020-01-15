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

no we got the the model and the data



13)

so we see we got all the model working and the data is generated
now we create the url pattern

look this pattern

there will be two "urls.py" 

1) in the Project BLOG
2) in the app blog [you have to create it]

your project URL will tells you which app you have to go
and your app URL tell you which logic you have to go
    
if the project URL is 'api'
and the app url is 'articles'
then your total URL will be

    => localhost:8000/api/articles

        

        1) go to the urls.py inside the BLOG project 

            you will see it tels you to include blog.urls
            that means urls.py inside the blog app
            but there is no urls.py inside a blog
            so we create a urls.py inside the blog 

        2) now dont add anything leave it blank 
            because we need to create a logic 
            then we add the logic with the app url


14) now we create  one logic .remember all the logic is written in the
    views.py file
    

        1) first we add another package 'rest_framework' in the 
            project settings.py
        2) now we use the API class from the rest framework 
            go to the views.py inside the blog app
            and wite a get method

    
15) now its time to add the logic with the app url
    so go to the urls.py inside the blog app which was empty 
    and connect to the logic

        go to the blog/urls.py

        1) we import the class from views.py and add a route

        ok now everything is done

        lets runthe server and go to the url

        localhost:8000/api/articles
        
        