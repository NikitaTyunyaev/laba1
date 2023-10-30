def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            diff = ord(i) + shift
            if i.islower(): #lowercase
                if diff > 122:
                    diff -= 122
                    diff += 97 - 1
            else:
                if diff > 90:
                    diff -= 90
                    diff += 90 -1
            ciphertext += chr(diff)
        else:
            ciphertext += i 
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            diff = ord(i) - shift
            if i.islower():
                if diff < 97:
                    diff -= 97
                    diff += 122 + 1
            else:
                if diff < 65:
                    diff -= 65
                    diff += 90 + 1
            plaintext += chr(diff)
        else:
             plaintext += i
    return plaintext
print(decrypt_caesar('Sbwkrq3.6'))

    