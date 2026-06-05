import numpy as np
import math

def hill_cipher(key, plain):
    key = key.replace(" ", "").upper()
    plain = plain.replace(" ", "").upper()

    while int(math.sqrt(len(key)))**2 != len(key):
        key += 'X'

    n = int(math.sqrt(len(key)))

    key_matrix = np.array([ord(c) - ord('A') for c in key]).reshape(n, n)

    # ✅ Display Matrix
    print("\nKey Matrix:")
    print(key_matrix)

    blocks = [plain[i:i+n] for i in range(0, len(plain), n)]

    if len(blocks[-1]) < n:
        blocks[-1] += 'X' * (n - len(blocks[-1]))

    cipher = ""

    for block in blocks:
        vector = np.array([ord(c) - ord('A') for c in block])
        result = np.matmul(key_matrix, vector) % 26
        cipher += ''.join(chr(int(num) + ord('A')) for num in result)

    return cipher

# Main
key = input("ENTER KEY: ")
plain = input("ENTER PLAIN TEXT: ")

cipher_text = hill_cipher(key, plain)
print("\nCIPHER TEXT:", cipher_text)