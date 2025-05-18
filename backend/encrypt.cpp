#include <openssl/aes.h>
#include <openssl/rand.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <ctime>

std::string generateHiddenDate() {
    time_t now = time(0);
    std::tm *ltm = localtime(&now);
    std::stringstream ss;
    ss << ltm->tm_year + 1900 << "-" << ltm->tm_mon + 1 << "-" << ltm->tm_mday;
    return ss.str();
}

void encryptText(const std::string& text, const std::string& outputFile, const unsigned char* key) {
    AES_KEY aesKey;
    AES_set_encrypt_key(key, 128, &aesKey);

    std::vector<unsigned char> buffer(text.begin(), text.end());
    unsigned char encrypted[16];

    AES_encrypt(buffer.data(), encrypted, &aesKey);

    std::ofstream out(outputFile);
    out << generateHiddenDate() << ":" << std::string(reinterpret_cast<char*>(encrypted), sizeof(encrypted));
    out.close();

    std::cout << "Texte crypté et sauvegardé dans : " << outputFile << std::endl;
}

int main() {
    unsigned char key[16] = "SuperSecureKey123";
    encryptText("Ce texte est confidentiel", "encrypted.txt", key);
    return 0;
}
