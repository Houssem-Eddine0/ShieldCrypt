from flask import Flask, request
from key_manager import get_key
import subprocess

app = Flask(__name__)

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    user_id = data["user_id"]
    date = data["date"]

    key = get_key(user_id, date)

    if key:
        subprocess.run(["./decrypt", "encrypted.txt", "decrypted.txt"])
        return {"message": "Décryptage réussi"}
    else:
        return {"error": "Clé non trouvée"}, 401

if __name__ == "__main__":
    app.run(debug=True)
