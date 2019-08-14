import json
from tweepy.streaming import StreamListener
from _persistence import Persistence


class OutStreamListener(StreamListener):
    def __init__(self):
        super().__init__
        self.__persistence = Persistence()

    def on_data(self, raw_data):
        try:
            tweet = self.format_json(raw_data)
            print(tweet)
            self.__persistence.inset_one(tweet)
        except BaseException as e:
            raise Exception("Error on_data: %s" % str(e))
            return True

    def on_error(self, status_code):
        print(status_code)

    @staticmethod
    def format_json(tweet):
        tweet = json.loads(tweet)
        return {"id": tweet["id"],
                "date_time": tweet["created_at"],
                "user_id" : tweet["user"]["id"],
                "user_name": tweet["user"]["name"],
                "user_screen_name": tweet["user"]["screen_name"],
                "user_screen_description": tweet["user"]["description"],
                "text": tweet["text"],
                "source": tweet["source"]}
