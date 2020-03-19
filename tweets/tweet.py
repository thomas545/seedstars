import sys
import json
import tweepy

# from tweets.models import Tweets, Links

#Get your Twitter API credentials and enter them here
consumer_key = "n3rmMdlMxTHxIuoa2eBwRlEDt"
consumer_secret = "2Zd2rqkOZboRzWRL4Y78b2rmoyaRboRjuDGP8fSwjNpdxAEUKk"
access_key = "840585628798582784-ps8EAVn7youITkj80sdEvarmezdDWFV"
access_secret = "Ejf7grmqnCrUrPPAKlUzojumf66M5iJ2iFlrLdp4V4zs6"

#method to get a user's last tweets
def get_or_create_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    user = api.get_user(username)

    user_tweets = tweepy.Cursor(api.user_timeline, screen_name=username).items(3)
    

    for t in user_tweets:
        print("fsdfsd")
        j = t._json
        urls = j.get("entities")['urls']
        created_at = j.get("created_at")
        text = j.get("text")
        name = j.get("user")['name']
        retweet_count = j.get("retweet_count")
        favorite_count = j.get("favorite_count")
        id = j.get("id")
        print(id)
            # TODO make serializer save
        # print(text == "Plot diagrams with #graphviz\n\nExample: 👇\n(`gv` code copied from fastai utils)\n\nimport graphviz\ndef gv(s): return gr… https://t.co/D7NlsrMim8")
        # for uri in urls:
        #     print(uri)
            # TODO make serializer save
            # for url, value in uri.items() :
            #     if url == "indices": continue
            #     print(url, value)
            # print("------------")

get_or_create_tweets('python_tip')