# Update description
# Lyle Hamm 11/20


class MangaFeed:
    def __init__(self, term, counts, api):
        self.term = term
        self.counts = counts
        self.api = api
        self.tweets = self.__get_data()

    def __get_data(self):
        tweets = self.api.search(q=self.term, count=self.counts)
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
                dictionary = {'url': url,
                              'twitter handle': tweet.user.screen_name,
                              'date posted': tweet.created_at,
                              'images': image_links}
                qtweets.append(dictionary)
        return qtweets

    def __str__(self):
        return 'Tracking data regarding tweets with both {} in the title and at ' \
               'least one image from a selection of {} posts.'.format(self.term, self.counts)

# feed = Manga_Feed("漫画", 100)
# print(feed)
# print(feed.data())
