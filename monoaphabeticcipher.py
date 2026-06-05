plain = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            index = plain.index(ch)
            result += key[index]
        else:
            result += ch
    return result


def decrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            index = key.index(ch)
            result += plain[index]
        else:
            result += ch
    return result


# ---- Main ----
key = input("Enter 26-letter key: ").lower()
text = input("Enter text: ").lower()

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)