from django.db import models



class Tweet(models.Model):
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    time_stamp = models.CharField(max_length=250, null=True, blank=True)
    python_tip = models.TextField(null=True, blank=True)
    who_posted = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=False)
    retweet_count = models.IntegerField(default=0)
    favorite_count = models.IntegerField(default=0)
    
    @staticmethod
    def create_tweets(id,time, tip, user, retweet=0, favorite=0, published=False):
        tweets = Tweet()
        tweets.tweet_id = id
        tweets.time_stamp = time
        tweets.python_tip = tip
        tweets.who_posted = user
        tweets.published = published
        tweets.retweet_count = retweet
        tweets.favorite_count = favorite
        tweets.save()
        return tweets


class Link(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='tweets', on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    expanded_url = models.CharField(max_length=200, null=True, blank=True)
    display_url = models.CharField(max_length=200, null=True, blank=True)
