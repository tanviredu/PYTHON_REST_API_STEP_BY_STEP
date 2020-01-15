from rest_framework import serializers
from .models import Article
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    body = serializers.CharField()
    ## add the author id
    author_id = serializers.IntegerField()

    def create(self,validated_data):
        return Article.objects.create(**validated_data)