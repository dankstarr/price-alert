import pymongo
import os


class Database(object):
    URI= os.environ.get('MONGODB_URI')
    database=None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.database = client['deploy']

    @staticmethod
    def find_one(collection, query):
        return Database.database[collection].find_one(query)

    @staticmethod
    def find(collection, query):
        return [i for i in Database.database[collection].find(query)]

    @staticmethod
    def insert(collection, data):
        Database.database[collection].insert(data)

    @staticmethod
    def update(collection, query, data):
        Database.database[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        Database.database[collection].remove(query)