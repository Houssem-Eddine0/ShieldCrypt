from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/")
db = client["ShieldCrypt"]
users_collection = db["Users"]
keys_collection = db["Keys"]

users_data = [
    {"name": "Alice Durand", "email": "alice@cryptexis.com", "class": "A"},
    {"name": "Bob Martin", "email": "bob@cryptexis.com", "class": "A"},
    {"name": "Clara Lefevre", "email": "clara@cryptexis.com", "class": "B"},
    {"name": "David Moreau", "email": "david@cryptexis.com", "class": "B"},
    {"name": "Eva Dubois", "email": "eva@cryptexis.com", "class": "C"},
    {"name": "Franck Bernard", "email": "franck@cryptexis.com", "class": "C"},
    {"name": "Gilles Lambert", "email": "gilles@cryptexis.com", "class": "C"},
    {"name": "Hugo Perrin", "email": "hugo@cryptexis.com", "class": "C"},
    {"name": "Inès Fontaine", "email": "ines@cryptexis.com", "class": "C"},
    {"name": "Jules Renault", "email": "jules@cryptexis.com", "class": "C"}
]

users_collection.insert_many(users_data)
print("10 utilisateurs ajoutés avec succès !")

def generate_key(user_id):
    return f"{user_id}-ABC123"

for user in users_collection.find():
    key_data = {
        "user_id": user["_id"],
        "key": generate_key(user["_id"]),
        "date": datetime.now(timezone.utc),
        "expiry": datetime.now(timezone.utc) + timedelta(days=7)
    }
    keys_collection.insert_one(key_data)

print("Clés générées et stockées avec succès !")
