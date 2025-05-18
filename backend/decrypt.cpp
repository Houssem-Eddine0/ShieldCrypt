#include <openssl/aes.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void decryptText(const std::string& inputFile, const std::string& outputFile, const unsigned char* key) {
    std::ifstream in(inputFile);
    std::string encryptedText;
    std::getline(in, encryptedText);

    std::string date = encryptedText.substr(0, 10);  // Extrait la date cachée
    std::string encryptedMessage = encryptedText.substr(11); // Contenu crypté

    AES_KEY aesKey;
    AES_set_decrypt_key(key, 128, &aesKey);

    unsigned char decrypted[16];
    AES_decrypt(reinterpret_cast<const unsigned char*>(encryptedMessage.c_str()), decrypted, &aesKey);

    std::ofstream out(outputFile);
    out << decrypted;
    out.close();

    std::cout << "Texte décrypté et sauvegardé dans : " << outputFile << std::endl;
}

int main() {
    unsigned char key[16] = "SuperSecureKey123";  // Clé récupérée depuis MongoDB
    decryptText("encrypted.txt", "decrypted.txt", key);
    return 0;
}
