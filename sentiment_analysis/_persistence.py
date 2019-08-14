import json
from pymongo import MongoClient


class Persistence:
    def __init__(self):
        self.__database = None
        self.__load_key()
        self.__connection = self.__get_connection()

    def __load_key(self):
        with open('keys.token') as file_token:
            key = file_token.read()

        key = json.loads(key)
        self.__database = key["database"]

    def __get_connection(self):
        con = MongoClient()
        db = con.get_database(self.__database)
        return db.twitter

    def inset(self, tweets):
        for tweet in tweets:
            self.__connection.insert_one(tweet)

    def inset_one(self, tweet):
        self.__connection.insert_one(tweet)

    def find_all(self):
        return self.__connection.find()

    def find(self, value):
        return self.__connection.find(value)
