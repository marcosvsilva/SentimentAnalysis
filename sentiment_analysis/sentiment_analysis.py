from _consumer import Consumer
from _persistence import Persistence
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


class Main:
    @staticmethod
    def analyst_tweets(hashtags, quantity_of_tweets):
        consumer = Consumer()
        consumer.consumer(hashtags, quantity_of_tweets)

        persistence = Persistence()

        ds = [dict(item) for item in persistence.find_all()]
        df = pd.DataFrame(ds)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df.text)

        word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
        word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
        word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
        print(word_count[:100])


if __name__ == '__main__':
    main = Main()

    hashtags = ["bolsonaro"]
    quantity_of_tweets = 50

    main.analyst_tweets(hashtags, quantity_of_tweets)
