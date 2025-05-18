from pymongo import MongoClient

# Connexion à la base MongoDB
client = MongoClient("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/?ssl=false")
db = client["ShieldCrypt"]

# Collections
users_collection = db["Users"]
keys_collection = db["Keys"]

print("Connexion réussie à MongoDB !")
