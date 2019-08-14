from _consumer import Consumer
from _persistence import Persistence
import pprint
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class Main:
    def __init__(self):
        pass

    @staticmethod
    def analyst_tweets():
        persistence = Persistence()

        ds = [dict(item) for item in persistence.find_all()]
        df = pd.DataFrame(ds)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df.text)

        word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
        word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
        word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
        print(word_count[:100])

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
    #main.list_saved_data()
    main.analyst_tweets()
