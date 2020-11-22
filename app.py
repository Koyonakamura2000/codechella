# template code borrowed from
# https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask

import tweepy
import config
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})


@app.route("/posttweet", methods=["GET", "POST"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def posttweet():
    # if POST request
    if request.method == "POST":
        jsonfile = request.get_json()
        print(jsonfile)
        print(jsonfile["id"])
        print(jsonfile["username"])
        print(jsonfile["formData"])
        reply(jsonfile["formData"], jsonfile["id"], jsonfile["username"])
        return "OK", 200
    return "hi"


def reply(user_inputs, post_id, username):
    status_text = "@" + username + "\n"
    status_text = status_text + "Hi there! Here's an English translation for each manga panel you posted! Courtesy of mangatranslator.com!\n"
    status_text = status_text + "あなたの漫画のセリフを英語に翻訳させていただきました！\n"
    for i in range(len(user_inputs)):
        status_text = status_text + '{}. {}\n'.format(i + 1, user_inputs[i])
    api.update_status(status=status_text, in_reply_to_status_id=post_id)
