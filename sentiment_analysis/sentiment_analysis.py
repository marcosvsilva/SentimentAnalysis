from _consumer import Consumer
from _persistence import Persistence
import pprint


class Main:
    def __init__(self):
        pass

    @staticmethod
    def consumer_twitter():
        consumer = Consumer()
        hashtags = ["bolsonaro"]
        consumer.consumer(hashtags)

    @staticmethod
    def list_saved_data():
        persistence = Persistence()
        for tweet in persistence.find_all():
            pprint.pprint(tweet)


if __name__ == '__main__':
    main = Main()
    #main.consumer_twitter()
    main.list_saved_data()
