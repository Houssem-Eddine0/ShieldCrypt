#include <openssl/aes.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void decryptText(const std::string& inputFile, const std::string& outputFile, const unsigned char* key) {
    std::ifstream in(inputFile, std::ios::binary);
    if (!in) {
        std::cerr << "Erreur: Impossible d'ouvrir le fichier crypté." << std::endl;
        return;
    }

    std::vector<unsigned char> encryptedMessage((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>());
    in.close();

    if (encryptedMessage.size() % AES_BLOCK_SIZE != 0) {
        std::cerr << "Erreur: Taille du texte chiffré incorrecte !" << std::endl;
        return;
    }

    AES_KEY aesKey;
    AES_set_decrypt_key(key, 128, &aesKey);

    std::vector<unsigned char> decrypted(encryptedMessage.size());
    for (size_t i = 0; i < encryptedMessage.size(); i += AES_BLOCK_SIZE) {
        AES_decrypt(&encryptedMessage[i], &decrypted[i], &aesKey);
    }

    std::ofstream out(outputFile, std::ios::binary);
    out.write(reinterpret_cast<char*>(decrypted.data()), decrypted.size());
    out.close();

    std::cout << "Texte décrypté et sauvegardé dans : " << outputFile << std::endl;
}

int main() {
    unsigned char key[16] = {0x53, 0x75, 0x70, 0x65, 0x72, 0x53, 0x65, 0x63, 
                         0x75, 0x72, 0x65, 0x4B, 0x65, 0x79, 0x31, 0x32}; // Clé récupérée depuis MongoDB
    decryptText("encrypted.txt", "decrypted.txt", key);
    return 0;
}
