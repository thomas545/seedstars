from rest_framework import serializers, exceptions

from .models import Tweet, Link, ContributePythonTip, TweetLike, TweetBookmark


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
        

class PythonTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContributePythonTip
        fields = "__all__"

    def validate(self, data):
        if ContributePythonTip.objects.filter(python_tip=data['python_tip']).exists():
            raise exceptions.ValidationError("This tip already exists")
        return data

class TweetMiniSerializer(serializers.ModelSerializer):
    link = LinksSerializer(source='tweets', many=True, read_only=True, required=False)
    class Meta:
        model = Tweet
        fields = "__all__"


class TweetLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetLike
        fields = "__all__"

    def validate(self, data):
        if TweetLike.objects.filter(tweet=data['tweet']).exists():
            raise exceptions.ValidationError("You already did like")
        return data


class TweetBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetBookmark
        fields = "__all__"

    def validate(self, data):
        if TweetBookmark.objects.filter(tweet=data['tweet']).exists():
            raise exceptions.ValidationError("You already bookmarked this tweet")
        return data

