
# WEP Encryption
def wep_encrypt(key, iv, plaintext):
    key_stream = generate_key_stream(key, iv, len(plaintext))
    print(key_stream)
    ciphertext = bytearray()

    for i in range(len(plaintext)):
        ciphertext.append(plaintext[i] ^ key_stream[i])

    return bytes(ciphertext)

# WEP Decryption (using the same key and IV)
def wep_decrypt(key, iv, ciphertext):
    key_stream = generate_key_stream(key, iv, len(ciphertext))
    plaintext = bytearray()

    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ key_stream[i])

    return bytes(plaintext)
    # WEP decryption is the same as encryption with the same key and IV

# Function to generate WEP key stream including IV
def generate_key_stream(key, iv, length):
    # Use some method to generate the key stream including IV (for demonstration, here IV is just concatenated to the key)
    full_key = key + iv
    key_stream = bytearray()
    while len(key_stream) < length:
        for k in full_key:
            key_stream.append(k)
    return key_stream[:length]

# Example usage:
key = b'\x11\x22\x33\x44\x55'
print(key)
iv = b'\x12\x34\x56'
print(iv)
message = b'Hello, this is a secret message!'

# Encryption
encrypted_data = wep_encrypt(key, iv, message)
print("Encrypted:", encrypted_data)

# Decryption using the same key and IV
decrypted_data = wep_decrypt(key, iv, encrypted_data)
print("Decrypted:", decrypted_data.decode('utf-8'))

# Display the IV used
print("Initialization Vector (IV):", iv)
