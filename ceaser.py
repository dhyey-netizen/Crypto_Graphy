# Caesar Cipher Encryption
def encrypt(text, shift):
    result = ""

    for ch in text:

        # For Uppercase Letters
        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char

        # For Lowercase Letters
        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result += new_char

        # For spaces/symbols/numbers
        else:
            result += ch

    return result


# Caesar Cipher Decryption
def decrypt(text, shift):
    result = ""

    for ch in text:

        # For Uppercase Letters
        if ch.isupper():
            new_char = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            result += new_char

        # For Lowercase Letters
        elif ch.islower():
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            result += new_char

        # For spaces/symbols/numbers
        else:
            result += ch

    return result


# Main Program
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)