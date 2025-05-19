from pymongo import MongoClient

client = MongoClient("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/")
db = client["ShieldCrypt"]
users_collection = db["Users"]

users_collection.delete_many({})
print("Tous les utilisateurs ont été supprimés !")
