import tweepy
import config

# Setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

# reference https://primetime.bluejeans.com/a2m/events/playback/18fa799a-d450-4799-b1e1-4a4519943353

tweets = api.search("#freemelee", count=10)

for tweet in tweets:
    print(tweet.text)