def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if 97 <= ord(plaintext[i]) <= 122 \
           or 65 <= ord(plaintext[i]) <= 90:
            if plaintext[i].islower():
                diff = ord(keyword[i % len(keyword)]) - 97
                different = ord(plaintext[i]) + diff
                if different > 122:
                    different -= 122
                    different += 97 - 1
            else:
                diff = ord(keyword[i % len(keyword)]) - 65
                different = ord(plaintext[i]) + diff
                if different > 90:
                    different -= 90
                    different += 65 - 1
            ciphertext += chr(different)
        else:
            ciphertext += plaintext[i]
    return ciphertext
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if 97 <= ord(ciphertext[i]) <= 122 \
           or 65 <= ord(ciphertext[i]) <= 90:
            if ciphertext[i].islower():
                diff = ord(keyword[i % len(keyword)]) - 97
                different = ord(ciphertext[i]) - diff
                if different < 97:
                    different -= 97
                    different += 122 + 1
            else:
                diff = ord(keyword[i % len(keyword)]) - 65
                different = ord(ciphertext[i]) - diff
                if different < 65:
                    different -= 65
                    different += 90 + 1
            plaintext += chr(different)
        else:
            plaintext += ciphertext[i]
    return plaintext
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
