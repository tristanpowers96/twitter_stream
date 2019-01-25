import tweepy
from tweepy import Stream, StreamListener, OAuthHandler
import json
import time

access_key = '334145792-ZMw7h2pVS9xeNE7hLnVqFBxTFyjH5SsjMCGeF3H2'
access_secret = 'HIWSHPVKlZV0PANNBAbiLZSM5tp2AxSVjmdOTJpE03Xmy'
consumer_key = '8DCGTfdBRQXEwaoqMx86IFwal'
consumer_secret = 'vex0Y1TqAlBxtEgYL6kTd4qH9mP7vCEUFJxXTW0r11LsDKr7t3'

class StreamListener(tweepy.StreamListener):
    #def __init__(self):
    #    self.start_time = time.time()
    #    self.limit = 10
    #    super(StreamListener, self).__init__()
    #def on_data(self, data):
    #    if (time.time() - self.start_time) < self.limit:
            #print("{} seconds elapsed\n".format(time.time() - self.start_time))
    #        return True
    #    else:
    #        return False
    def on_status(self, status):
        tweet = status._json
        print("""
        User: {}
        Tweet: {}
        Hastags: {}
        Posted at: {}
        """.format(tweet["user"]["screen_name"], tweet["text"], [tag for tag in tweet["entities"]["hashtags"]["text"]], tweet["created_at"]))
        with open('tweets.json', 'a') as file:
            file.write(json.dumps(status._json, indent=4))

    def on_error(self, status_code):
        if status_code == 420:
            print("Rate limit reached")
            return False

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#limits = api.rate_limit_status()
stream_listener = StreamListener()

local_tweets = Stream(auth, listener=stream_listener)
local_tweets.filter(languages=["en"], track=['a,the,to,at,or,in,on,be,it,he,she'])
#local_tweets.sample()
#local_tweets.disconnect()
