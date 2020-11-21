# using example import data
import tweepy
import config
import json


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

filename = "home.html"
html = open(filename, "w", encoding="utf-8")
html.write("<html><head><link href=\"style.css\" rel=\"stylesheet\"/><title>Voluntary Twitter Manga Translation Feed</title></head>")
html.write("<body>")
# data needed
# url of tweet
# array of photos (if possible)
# date posted
# Twitter handle of author


def get_embed(url):
    embedjson = api.get_oembed(url=url, maxwidth=500, align="center")
    return embedjson["html"]


def write_block(url):
    tweet = get_embed(url)
    button = "<button class=\"translatebtn\" type=\"button\">Translate</button>"
    html.write("<div class=\"side-by-side\">")
    html.write("<div class=\"form\">")
    html.write("<")
    html.write(button)
    html.write("</div>")
    html.write(tweet)
    html.write("</div>")


testurl = "https://twitter.com/kurita_aguri/status/1329752551210639367"
write_block(testurl)

html.write("</body>")
html.write("</html>")