from pymongo import MongoClient
from .APIkey import MONGODB_URI


def connect_to_mongodb():
    client = MongoClient(MONGODB_URI)
    db = client.my_database
    return db