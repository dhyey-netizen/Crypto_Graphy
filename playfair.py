def generate_matrix(key):
    key = key.replace("j", "i")
    matrix = []
    used = ""

    for ch in key:
        if ch not in used and ch.isalpha():
            used += ch

    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in used and ch != "j":
            used += ch

    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))

    return matrix


def find_position(matrix, ch):
    for i in range(5):
         for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def encrypt(text, matrix):
    text = text.replace("j", "i")
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "x"

        if a == b:
            b = "x"
            i += 1
        else:
            i += 2

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # same row
            result += matrix[r1][(c1+1)%5]
            result += matrix[r2][(c2+1)%5]

        elif c1 == c2:  # same column
            result += matrix[(r1+1)%5][c1]
            result += matrix[(r2+1)%5][c2]

        else:  # rectangle
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def decrypt(text, matrix):
    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1]
        i += 2

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5]
            result += matrix[r2][(c2-1)%5]

        elif c1 == c2:
            result += matrix[(r1-1)%5][c1]
            result += matrix[(r2-1)%5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# ---- Main ----
key = input("Enter key: ")
text = input("Enter text: ")

matrix = generate_matrix(key)
print("Playfair Matrix:")
for row in matrix:
    print(row)
encrypted = encrypt(text, matrix)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, matrix)
print("Decrypted:", decrypted)