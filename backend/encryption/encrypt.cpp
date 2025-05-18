#include <openssl/aes.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <sstream>

#define AES_BLOCK_SIZE 16

std::string generateHiddenDate() {
    time_t now = time(0);
    std::tm *ltm = localtime(&now);
    std::stringstream ss;
    ss << ltm->tm_year + 1900 << ltm->tm_mon + 1 << ltm->tm_mday; // Format compact
    return ss.str();
}

void encryptText(const std::string& text, const std::string& outputFile, const unsigned char* key) {
    AES_KEY aesKey;
    AES_set_encrypt_key(key, 128, &aesKey);

    // Ajuster la taille du texte pour AES (padding si nécessaire)
    std::vector<unsigned char> buffer(text.begin(), text.end());
    while (buffer.size() % AES_BLOCK_SIZE != 0) {
    buffer.push_back(0);  // Ajout de padding avec des zéros
}


    std::vector<unsigned char> encrypted(buffer.size());

    for (size_t i = 0; i < buffer.size(); i += AES_BLOCK_SIZE) {
        AES_encrypt(&buffer[i], &encrypted[i], &aesKey);
    }

    std::ofstream out(outputFile, std::ios::binary);
    out.write(generateHiddenDate().c_str(), generateHiddenDate().size());  // Ajout de la date cachée
    out.write(reinterpret_cast<char*>(encrypted.data()), encrypted.size());
    out.close();

    std::cout << "Texte crypté et sauvegardé dans : " << outputFile << std::endl;
}

int main() {
    unsigned char key[16] = {0x53, 0x65, 0x63, 0x75, 0x72, 0x65, 0x4B, 0x65, 
                         0x79, 0x5F, 0x31, 0x32, 0x38, 0x62, 0x69, 0x74}; 
    encryptText("Ce texte est confidentiel", "encrypted.txt", key);
    return 0;
}
