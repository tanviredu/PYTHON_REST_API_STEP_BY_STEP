from django.shortcuts import render,get_object_or_404

## import the Response from the restapi 
from rest_framework.response import Response
from rest_framework.views import APIView

## import the model
from .models import Article

## now all our function will be inside the API derived class
## because we need APi

from .serializers import ArticleSerializer

class Articleview(APIView):
    def get(self,request):
        ## get all the articles
        articles = Article.objects.all()
        ## return to response
        ## added the serializer

        serializer = ArticleSerializer(articles,many=True)

        ## many=true means we fetch multiple data 

        return Response({"articles":serializer.data})

    # def get(self,request,pk):
    #     article = get_object_or_404(Article.objects.all(),pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response({"article":serializer.data})


    def post(self,request):
        ## get the post JSON with the key
        article = request.data.get('article')
        #serialize it
        serializer = ArticleSerializer(data=article)

        ## chack is data is valid
        if serializer.is_valid(raise_exception=True):
            ##save the article
            article_saved = serializer.save()
        
        ## now send the data to output
        return Response({"Success":"Article '{}' created successfully".format(article_saved.title)})


    def put(self,request,pk):
        ## fetch the article
        saved_article = get_object_or_404(Article.objects.all(),pk=pk)
        ##get the new data
        data = request.data.get('article')
        ##send it to the serializer
        serializer = ArticleSerializer(instance=saved_article,data=data,partial=True)

        ## partial=True means it can parial edit the document

        if serializer.is_valid(raise_exception=True):
            ## save the article
            article_saved = serializer.save()

        ##return the data
        return Response({"success":"Article '{}' updated sucessfully".format(article_saved.title)})

    def delete(self,request,pk):

        ## get the object first
        article = get_object_or_404(Article.objects.all(),pk=pk)
        ## delete it
        article.delete()
        ## return the success message
        return Response({"message":"Article id '{}' is deleted".format(pk)})

class SingleArticlePost(APIView):
     def get(self,request,pk):
         article = get_object_or_404(Article.objects.all(),pk=pk)
         serializer = ArticleSerializer(article)
         return Response({"article":serializer.data})