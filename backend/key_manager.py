from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://votre_url_mongodb")
db = client["ShieldCrypt"]
collection = db["Keys"]

def store_key(user_id, key):
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(days=7)  # Archive par semaine
    collection.insert_one({"user_id": user_id, "key": key, "expiry": expiration_date})
    print(f"Clé stockée pour {user_id} : {key}")

def get_key(user_id, date):
    key_entry = collection.find_one({"user_id": user_id, "expiry": {"$gte": date}})
    return key_entry["key"] if key_entry else None
