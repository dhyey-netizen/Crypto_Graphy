import random
from math import gcd

# Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find d
def find_d(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d

# -------- INPUT --------
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not is_prime(p) or not is_prime(q):
    print("Both must be prime!")
    exit()

# Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# 🔥 Random e generation
while True:
    e = random.randint(2, phi - 1)
    if gcd(e, phi) == 1:
        break

# Find d
d = find_d(e, phi)

# Keys
print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Message
M = int(input("\nEnter message: "))

# Encrypt
C = pow(M, e, n)
print("Encrypted:", C)

# Decrypt
original = pow(C, d, n)
print("Decrypted:", original)