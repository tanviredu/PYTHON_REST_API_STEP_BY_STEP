from django.shortcuts import render

## import the Response from the restapi 
from rest_framework.response import Response
from rest_framework.views import APIView

## import the model
from .models import Article

## now all our function will be inside the API derived class
## because we need APi

class ArticleView(APIView):
    def get(self,request):
        ## get all the articles
        articles = Article.objects.all()
        ## return to response
        return Response({"articles":articles})
