import json
from pymongo import MongoClient

def load_json_to_mongo():
    client = MongoClient("mongodb://root:root@localhost:27017/")
    db = client["walmart"]
    collection = db["api_product"]

    with open("data.json") as f:
        data = json.load(f)

    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)


load_json_to_mongo()

