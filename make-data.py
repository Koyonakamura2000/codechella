import tweepy, config

# testing
# create a config.py with the template below, with fields entered appropriately from developer.twitter.com:
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


# reference https://primetime.bluejeans.com/a2m/events/playback/18fa799a-d450-4799-b1e1-4a4519943353

# Update description
# Lyle Hamm 11/20


class Manga_Feed():
    def __init__(self, term, counts):
        self.term = term
        self.counts = counts

    def data(self):
        tweets = api.search(q=self.term, count=self.counts)
        qtweets = []
        for tweet in tweets:
            if tweet.user.followers_count >= 0 and \
                    tweet.user.verified == False and \
                    tweet.favorite_count >= 0 and \
                    tweet.is_quote_status == False and \
                    'media' in tweet.entities.keys():
                image_links = []
                url = tweet.entities['media'][0]['expanded_url']
                for i in tweet.extended_entities['media']:
                    image_links.append(tweet.extended_entities['media'][0]['media_url'])
                dict = {'url': url,
                        'twitter handle': tweet.user.screen_name,
                        'date posted': tweet.created_at,
                        'images': image_links}
                qtweets.append(dict)
        print(qtweets)
        return qtweets

    def __str__(self):
        return 'Tracking data regarding tweets with both {} in the title and at ' \
               'least one image from a selection of {} posts.'.format(self.term, self.counts)


# feed = Manga_Feed("漫画", 100)
# print(feed)
# print(feed.data())
