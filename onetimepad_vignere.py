import string
import random

# Generate Key
def generate_key(plain_txt):
    chars = string.ascii_uppercase
    key = "".join(random.choices(chars, k=len(plain_txt)))
    return key

# One Time Pad
def onetimePadEncrypt(key, plain):
    result = ""
    for i in range(len(key)):
        p = ord(plain[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        temp = (p + k) % 26
        result += chr(ord('A') + temp)
    return result

def onetimePadDecrypt(key, cipher):
    result = ""
    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        temp = (c - k) % 26
        result += chr(temp + ord('A'))
    return result

# Vigenere: Using Repeated Key
def repeat_key(key, plain_txt_len):
    result = ""
    k = 0
    for _ in range(plain_txt_len):
        result += key[k]
        k = (k + 1) % len(key)
    return result

# Vigenere: Using Auto Key
def auto_key(key, plain_txt):
    for p in plain_txt:
        if len(key) < len(plain_txt):
            key += p
    return key

def vigenere_encryption(key, plain):
    result = ""
    for i in range(len(plain)):
        p = ord(plain[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        temp = (p + k) % 26
        result += chr(ord('A') + temp)
    return result

def vigenere_decryption(key, cipher):
    result = ""
    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        temp = (c - k) % 26
        result += chr(ord('A') + temp)
    return result

# Vigenere: Using Table
def generate_table():
    table = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        row = alphabets[i:] + alphabets[:i]
        table.append(row)
    return table

def vigenere_table_encrypt(key, plain):
    table = generate_table()
    result = ""
    for i in range(len(plain)):
        row = ord(key[i]) - ord('A')
        col = ord(plain[i]) - ord('A')
        result += table[row][col]
    return result

def main():
    plain_txt = input('ENTER PLAIN TEXT: ').upper().replace(" ", "")
    key = input("ENTER KEY: ").upper().replace(" ", "")

    # One Time Pad
    otp_key = generate_key(plain_txt)
    otp_cipher = onetimePadEncrypt(otp_key, plain_txt)
    otp_plain = onetimePadDecrypt(otp_key, otp_cipher)

    print("\nONE TIME PAD")
    print(">> Key Used:", otp_key)
    print(">> Cipher Text:", otp_cipher)
    print(">> Plain Text:", otp_plain)

    # Vigenere (Repeated Key)
    rep_key = repeat_key(key, len(plain_txt))
    rep_cipher = vigenere_encryption(rep_key, plain_txt)
    rep_plain = vigenere_decryption(rep_key, rep_cipher)

    print("\nVIGENERE (REPEATED KEY)")
    print(">> Key Used:", rep_key)
    print(">> Cipher Text:", rep_cipher)
    print(">> Plain Text:", rep_plain)

    # Vigenere (Auto Key)
    autoKey = auto_key(key, plain_txt)
    auto_cipher = vigenere_encryption(autoKey, plain_txt)
    auto_plain = vigenere_decryption(autoKey, auto_cipher)

    print("\nVIGENERE (AUTO KEY)")
    print(">> Key Used:", autoKey)
    print(">> Cipher Text:", auto_cipher)
    print(">> Plain Text:", auto_plain)

    # Vigenere (Using Table)
    table_cipher = vigenere_table_encrypt(rep_key, plain_txt)

    print("\nVIGENERE TABLE (REPEATED KEY)")
    print(">> Cipher Text:", table_cipher)

if __name__ == "__main__":
    main()