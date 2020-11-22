import tweepy, config, json

# testing

# Setup authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# reference https://primetime.bluejeans.com/a2m/events/playback/18fa799a-d450-4799-b1e1-4a4519943353

# get url of the tweet, get photos if possible, author name, date posted

tweets = api.search(q="漫画", count=10)
print(tweets[0]._json)

# class Manga_Feed():
#     def __init__(self, term, counts):
#         self.term = term
#         self.counts = counts
#
#     def data(self):
#         tweets = api.search(q=self.term, count=self.counts)
#         qtweets = []
#         for tweet in tweets:
#             if tweet.user.followers_count >= 0 and \
#                     tweet.user.verified == False and \
#                     tweet.favorite_count >= 0 and \
#                     tweet.is_quote_status == False and \
#                     'media' in tweet.entities.keys():
#                 image_links = []
#                 url = tweet.entities['media'][0]['expanded_url']
#                 for i in tweet.extended_entities['media']:
#                     image_links.append(tweet.extended_entities['media'][0]['media_url'])
#                 dictionary = {'url': url,
#                               'post_id': tweet._json['id'],
#                               'twitter_handle': tweet.user.screen_name,
#                               'date_posted': tweet.created_at,
#                               'images': image_links}
#                 qtweets.append(dictionary)
#         return qtweets
#
#     def __str__(self):
#         return 'Tracking data regarding tweets with both {} in the title and at ' \
#                'least one image from a selection of {} posts.'.format(self.term, self.counts)
#
#
# feed = Manga_Feed(term = '漫画', counts = 30)
# print(feed.data())
#
#
# def reply(user_inputs, post_id, username):
#     status_text = "@" + ""
#     status_text = status_text + "Hi there! Here's an English translation for each manga panel you posted! Courtesy of mangatranslator.com!\n"
#     status_text = status_text + "あなたの漫画のセリフを英語に翻訳させていただきました！\n"
#     for i in range(len(user_inputs)):
#         status_text = status_text + '{}. {}\n'.format(i + 1, user_inputs[i])
#     print(status_text)
#     api.update_status(status=status_text, in_reply_to_status_id=post_id)


