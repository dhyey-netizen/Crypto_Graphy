from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# -------------------------------
# STEP 1: Define 64-bit key
# DES requires exactly 8 bytes = 64 bits
# -------------------------------
key = b'ABCDEFGH'   # 8-byte key (64-bit)

# -------------------------------
# STEP 2: Create DES Cipher Object
# MODE_ECB = Electronic Code Book mode
# (simplest mode for demonstration)
# -------------------------------
cipher = DES.new(key, DES.MODE_ECB)

# -------------------------------
# STEP 3: Input Plaintext (64-bit block)
# DES works on 8-byte blocks
# If data is smaller, we pad it
# -------------------------------
plaintext = b'HELLO123'   # exactly 8 bytes (64 bits)

# -------------------------------
# STEP 4: Padding (if needed)
# Ensures input is multiple of 8 bytes
# -------------------------------
padded_text = pad(plaintext, DES.block_size)

# -------------------------------
# STEP 5: Encrypt Data
# Internally DES performs:
#   - Initial Permutation (IP)
#   - 16 Rounds:
#       1. Expansion Permutation (E)
#       2. XOR with round key
#       3. S-Box Substitution (non-linear step)
#       4. P-Box Permutation (rearrangement)
#   - Final Permutation (FP)
# -------------------------------
ciphertext = cipher.encrypt(padded_text)

# -------------------------------
# STEP 6: Display Output
# -------------------------------
print("Plaintext :", plaintext)
print("Ciphertext (in hex):", ciphertext.hex())