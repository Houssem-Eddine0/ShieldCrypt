// Fonction pour basculer la visibilité du mot de passe
document.querySelector('.password-toggle').addEventListener('click', function() {
    const passwordField = document.getElementById('password');
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        this.textContent = 'Masquer';
    } else {
        passwordField.type = 'password';
        this.textContent = 'Afficher';
    }
});
