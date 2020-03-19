import sys
import json
import tweepy
from django.shortcuts import get_object_or_404
from .models import Tweet, Link
from . import serializers
from rest_framework import views, viewsets, generics, response, exceptions, status, filters
from django_filters.rest_framework import DjangoFilterBackend

#Get your Twitter API credentials and enter them here
consumer_key = "n3rmMdlMxTHxIuoa2eBwRlEDt"
consumer_secret = "2Zd2rqkOZboRzWRL4Y78b2rmoyaRboRjuDGP8fSwjNpdxAEUKk"
access_key = "840585628798582784-ps8EAVn7youITkj80sdEvarmezdDWFV"
access_secret = "Ejf7grmqnCrUrPPAKlUzojumf66M5iJ2iFlrLdp4V4zs6"



class CreateTweets(views.APIView):
    def post(self, request, *args, **kwargs):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        user = api.get_user('python_tip')
        user_tweets = tweepy.Cursor(api.user_timeline, screen_name='python_tip').items()

        for t in user_tweets:
            j = t._json
            urls = j.get("entities")['urls']
            created_at = j.get("created_at")
            text = j.get("text")
            id = j.get("id")
            name = j.get("user")['name']
            retweet_count = j.get("retweet_count")
            favorite_count = j.get("favorite_count")
            if Tweet.objects.filter(python_tip=text): continue

            tweets = Tweet().create_tweets(id, created_at, text, name, retweet_count, favorite_count, True)
            for uri in urls:
                serializer = serializers.LinksSerializer(data=uri)
                serializer.is_valid(raise_exception=True)
                serializer.save(tweet=tweets)           

        return response.Response("Done", status=status.HTTP_200_OK)



class ListTweetsView(generics.ListAPIView):
    serializer_class = serializers.TweetSerializer
    queryset = Tweet.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['published', 'retweet_count', 'favorite_count']
    search_fields = ['python_tip']

    
class RetweetTweets(views.APIView):
    def post(self, request, *args, **kwargs):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        tweets = Tweet.objects.all()
        for tweet in tweets:
            api.retweet(tweet.tweet_id)
        return response.Response("Retweeted all tweets successfully.")