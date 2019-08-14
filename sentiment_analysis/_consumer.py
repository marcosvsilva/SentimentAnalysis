import json
import oauth2 as oauth
import urllib.parse


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

    def __connection(self):
        consumer = oauth.Consumer(self.__key, self.__secret)
        token = oauth.Token(self.__access_key, self.__access_secret)
        return oauth.Client(consumer, token)

    def consumer(self, hashtag):
        connection = self.__connection()
        url_request = "https://api.twitter.com/1.1/search/tweets.json?q=%s" % urllib.parse.quote(hashtag, safe='')

        try:
            request = connection.request(url_request)
            response = json.loads(request[1].decode())['statuses']
        except Exception as e:
            raise Exception(e)

        return response
