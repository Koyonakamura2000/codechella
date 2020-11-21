# using example import data
import tweepy
import config
import json
import urllib.request
from codechella.make_data import MangaFeed

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

filename = "home.html"
html = open(filename, "w", encoding="utf-8")
html.write(
    "<html><head><link href=\"style.css\" rel=\"stylesheet\"/><title>Voluntary Twitter Manga Translation Feed</title></head>")
html.write("<body>")

# data needed
# url of tweet
# array of photos (if possible)
# date posted
# Twitter handle of author


mangaFeed = MangaFeed("漫画", 15, api)
print(mangaFeed)
feed = mangaFeed.tweets
print(len(feed))
for post in feed:
    print(post)
    print(post["images"])


# makes a form input line, where users can input a translation for one photo. num refers to the photo number
def make_form_line(num):
    return "<p><label>Translation for line " + str(num) + ": <input type=\"text\"/></label></p>"


def get_embed(url):
    embedjson = api.get_oembed(url=url, maxwidth=500, align="center")
    return embedjson["html"]


# writes a block for one tweet - embedded tweet and form fields based on number of images
def write_block(tweet):
    tweetembed = get_embed(tweet["url"][:-8])
    html.write("<div class=\"side-by-side\">")
    # form div contains textboxes and translate button
    html.write("<div class=\"form\">")
    for i in range(len(tweet["images"])):
        html.write(make_form_line(i+1))
    html.write("<button class=\"translatebtn\" type=\"button\">Translate</button>")
    html.write("</div>")
    html.write(tweetembed)
    html.write("</div>")


#iterate through the tweets and make blocks for each
for tweet in feed:
    write_block(tweet)

html.write("</body>")
html.write("</html>")
