import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='tweets')

c = conn.cursor()

ckey = "hRNLzt3eIxSmSdyR7AZYo7tX6"
csecret = "lfvK9Knc47vdYqK9STa0LzUwqwGPyaHukhRH9HG8dutTt2glEZ"
atoken = "81080657-XO1oal47uPWikhjCK5EFaW9dt1FvsbyJJQ45GToX0"
asecret = "kvjNLExUpGNN7rcXu5vpoehktf0Fu9MI9blSfEAqJKSvl"

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        post = all_data["text"]
        username = all_data["user"]["screen_name"]

        c.execute("INSERT INTO tweets (time, username, post) VALUES (%s,%s,%s)",
            (time.time(), username, post))

        conn.commit()

        print(username, post)

        return True

    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["jokowi"])