import tweepy
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'IraZ9ogP5gxDDgKSnbLSDYBhp'
consumer_secret = 'n85R8n9SS3YUxbe9RRSEXHbPCCf0BhuyRCVsp0NScSBoiueOWf'
access_token = '3146887867-l8QXXfGMwTbiJlZFJo56By45Qs7Kb8xTHBdvtLp'
access_token_secret = 'BNTP1wSA9wL9vPLmDiZFVX2B4T4YtdMXUle8wXlxnTV2V'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])