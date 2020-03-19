from rest_framework import serializers

from .models import Tweet, Link


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"
        extra_kwargs = {'tweet':{'required': False}}
        
class TweetSerializer(serializers.ModelSerializer):
    link = LinksSerializer(source='tweets', many=True)
    class Meta:
        model = Tweet
        fields = "__all__"
        