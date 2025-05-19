from pymongo import MongoClient
from datetime import datetime, timezone, timedelta

client = MongoClient("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/")
db = client["ShieldCrypt"]
users_collection = db["Users"]
keys_collection = db["Keys"]

users_data = [
    {"name": "Alice Durand", "email": "alice@cryptexis.com", "password": "Alice123", "class": "A"},
    {"name": "Bob Martin", "email": "bob@cryptexis.com", "password": "Bob456", "class": "A"},
    {"name": "Clara Lefevre", "email": "clara@cryptexis.com", "password": "Clara789", "class": "B"},
    {"name": "David Moreau", "email": "david@cryptexis.com", "password": "David321", "class": "B"},
    {"name": "Eva Dubois", "email": "eva@cryptexis.com", "password": "Eva654", "class": "C"},
    {"name": "Franck Bernard", "email": "franck@cryptexis.com", "password": "Franck987", "class": "C"},
    {"name": "Gilles Lambert", "email": "gilles@cryptexis.com", "password": "Gilles741", "class": "C"},
    {"name": "Hugo Perrin", "email": "hugo@cryptexis.com", "password": "Hugo852", "class": "C"},
    {"name": "Inès Fontaine", "email": "ines@cryptexis.com", "password": "Ines963", "class": "C"},
    {"name": "Jules Renault", "email": "jules@cryptexis.com", "password": "Jules369", "class": "C"}
]

users_collection.insert_many(users_data)
print("10 utilisateurs ajoutés avec des mots de passe sans hachage !")

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
