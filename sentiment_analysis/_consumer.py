from tweepy import OAuthHandler
from tweepy import Stream
from _out_stream import OutStreamListener
import json


class Consumer:
    def __init__(self):
        self.__key = None
        self.__secret = None
        self.__access_key = None
        self.__access_secret = None
        self.__load_key()

    def __load_key(self):
        with open('keys.token') as file_token:
            key = file_token.read()

        key = json.loads(key)
        self.__key = key["key"]
        self.__secret = key["token"]
        self.__access_key = key["access_key"]
        self.__access_secret = key["access_token"]

    def __get_connection(self, quantity_tweets):
        out_stream = OutStreamListener(quantity_tweets)
        auth = OAuthHandler(self.__key, self.__secret)
        auth.set_access_token(self.__access_key, self.__access_secret)

        return Stream(auth, out_stream)

    def consumer(self, hashtags, quantity_tweets):
        try:
            stream = self.__get_connection(quantity_tweets)
            stream.filter(track=hashtags)
        except Exception as e:
            print("Error: %s" % e)
        except KeyboardInterrupt:
            pass

        stream.disconnect()
