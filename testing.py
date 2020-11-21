import tweepy
import config
import pycountry
import json


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


# testing
# create a config.py with the template below, with fields entered appropriately from developer.twitter.com:
# consumer_key = ""
# consumer_key_secret = ""
# access_token = ""
# access_token_secret = ""

# Setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# reference https://primetime.bluejeans.com/a2m/events/playback/18fa799a-d450-4799-b1e1-4a4519943353
# tweepy reference: http://docs.tweepy.org/en/latest/api.html

tweets = api.search("漫画", result_type="mixed", count=3)

print(pretty(tweets[1]._json))
# https://developer.twitter.com/en/docs/twitter-for-websites/timelines/guides/oembed-api