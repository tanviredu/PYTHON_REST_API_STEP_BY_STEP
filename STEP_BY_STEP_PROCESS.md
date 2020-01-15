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

