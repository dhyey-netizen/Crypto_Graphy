import hashlib

# Caesar Cipher Encryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def send_message(data, shift):
    # Step 1: Generate SHA-256 hash
    hash_value = hashlib.sha256(data.encode()).hexdigest()

    # Step 2: Combine message + hash
    combined = data + "xx" + hash_value

    # Step 3: Encrypt full combined message
    encrypted_message = caesar_encrypt(combined, shift)

    return encrypted_message

# Example
message = "Salary updated to 50000"
shift = 3

sent_message = send_message(message, shift)

print("Encrypted Message Sent:")
print(sent_message)

# /* hashing part2 */
import hashlib

# Caesar Cipher Decryption
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def receive_message(received_message, shift):
    try:
        # Step 1: Decrypt message
        decrypted = caesar_decrypt(received_message, shift)

        # Step 2: Split message and hash
        data, received_hash = decrypted.split("xx")

        # Step 3: Generate new hash
        new_hash = hashlib.sha256(data.encode()).hexdigest()

        # Step 4: Compare hashes
        if new_hash == received_hash:
            print("✅ Message is authentic and not modified")
            print("Message:", data)
        else:
            print("❌ Message has been tampered")

    except:
        print("❌ Invalid message format")

# Example (paste sender output here)
received_message = input("Enter received encrypted message: ")
shift = 3

receive_message(received_message, shift)