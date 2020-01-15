from django.db import models


## create the author model

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    ## this is the decorator function

    def __str__(self):
        return self.name 


## this is Article Model

class Article(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()

    ## this is the foreign key
    author = models.ForeignKey('Author',related_name='articles',on_delete=models.CASCADE)

    ## this foreign key connect the author field to the author Table
    # and if the author got deleted the post of all of its will be 
    # deleted too

    def __str__(self):
        return self.title 


