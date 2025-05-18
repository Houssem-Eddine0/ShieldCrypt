def check_users():
    users = users_collection.find()
    for user in users:
        print(f"Utilisateur : {user['name']} | Classe : {user['class']} | Email : {user['email']}")

def check_keys():
    keys = keys_collection.find()
    for key in keys:
        print(f"Clé de {key['user_id']} → {key['key']} | Expire le : {key['expiry']}")

check_users()
check_keys()
