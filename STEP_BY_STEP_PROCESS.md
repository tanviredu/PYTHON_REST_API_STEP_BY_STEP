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



11) data , we need a lot of data to play with
    so we use the seeder for generating the data
    and we change some core library to make this work
    because this library is buggy

    1) add the 'django_seed' to the settings.py in the project
    go to the settings.py

    2) go to the folder
        venv/lib/site-packages/django_seed

        and inside there is a file called "__init__.py"

        open it and go to the "faker" function 

        go to line 35

        and change the line

        from:
            cls.fakers[code].seed(random.randint(1, 10000))

        to:
            cls.fakers[code].seed_instance(random.randint(1, 10000))

        go and see the __init__.py file

    3) 
        we import the seeder and fill the 
        table with fake data
        100 users and 200 Article
        we use the Faker Service to do that 

        in this step you also see how the interactive way to
        manipulate data
        
        run command
        => python3 manage.py shell

        it will open a python shell

        >>> from django_seed import Seed
        >>> from blog.models import Author,Article
        >>> seeder = Seed.seeder()
        >>> seeder.add_entity(Author,100,{'name':lambda x:seeder.faker.name(),'email':lambda x:seeder.faker.email()})
        >>> seeder.add_entity(Article,200)
        >>> seeder.execute()

        exit the shell 

        [explanation
            we just import the model
            and added the fake data with seeder
        ]
    
    4) add the models in the admin.py inside the app
        go to the admin.py and register 

    5) now run the server and go to the admin panel and 
    see if the data is there

        