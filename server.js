const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const app = express();

// Middleware pour gérer les requêtes
app.use(express.static("frontend"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Connexion à MongoDB avec gestion des erreurs
mongoose.connect("mongodb+srv://shieldcrypt:4gBn9ZMoRj3opvDx@cluster0.l4siktg.mongodb.net/ShieldCrypt")
    .then(() => console.log("✅ Connexion réussie à MongoDB"))
    .catch(err => console.error("❌ Erreur de connexion à MongoDB :", err));

// Modèle utilisateur
const userSchema = new mongoose.Schema({ name: String, email: String, password: String });
const User = mongoose.model("User", userSchema);

// Route principale
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "frontend", "page_de_connexion", "page_accueil.html"));
});

// Route de connexion utilisateur
app.post("/login", async (req, res) => {
    try {
        const { email, password } = req.body;
        console.log("🔎 Tentative de connexion :", email);

        if (!email || !password) {
            return res.status(400).json({ success: false, message: "Tous les champs sont requis !" });
        }

        const user = await User.findOne({ email });

        if (!user || user.password !== password) {
            return res.status(401).json({ success: false, message: "Identifiants incorrects" });
        }

        console.log("✅ Connexion réussie :", email);
        res.status(200).json({ success: true, redirect: "/choix_action.html" });

    } catch (error) {
        console.error("❌ Erreur lors de la connexion :", error);
        res.status(500).json({ success: false, message: "Erreur interne du serveur" });
    }
});

// Démarrer le serveur
const PORT = 5000;
app.listen(PORT, () => console.log(`🚀 Serveur Express démarré sur http://127.0.0.1:${PORT}`));
