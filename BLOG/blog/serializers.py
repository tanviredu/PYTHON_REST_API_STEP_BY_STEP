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

    def update(self,instance,validated_data):
        ## changing the attribute of the instance
        ## and replaece the data with the new validated data
        ## if we provide data it will be replaced
        ## otherwise the old one will be assigned
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.body = validated_data.get('body',instance.body)
        instance.author_id = validated_data.get('author_id',instance.author_id)

        ##save the updated data
        instance.save()
        return instance