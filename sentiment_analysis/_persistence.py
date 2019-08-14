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

    def inset(self, twitter):
        for twit in twitter:
            self.__connection.insert_one(twit)

    def find_all(self):
        self.__connection.findall()

    def find(self, value):
        self.__connection.find(value)
