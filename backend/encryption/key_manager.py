from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/")
db = client["ShieldCrypt"]
keys_collection = db["Keys"]

def get_key(user_id, date):
    key_entry = keys_collection.find_one({"user_id": user_id, "expiry": {"$gte": date}})
    return key_entry["key"] if key_entry else None
