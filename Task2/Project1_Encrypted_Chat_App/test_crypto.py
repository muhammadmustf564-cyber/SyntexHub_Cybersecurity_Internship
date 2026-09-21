from crypto_utils import encrypt_message, decrypt_message

message = "Hello, this is a secret message!"

print("Original message:")
print(message)

encrypted = encrypt_message(message)

print("\nEncrypted data:")
print(encrypted)

decrypted = decrypt_message(encrypted)

print("\nDecrypted message:")
print(decrypted)

print("\nTesting tampered message...")

tampered = bytearray(encrypted)
tampered[-1] ^= 1

try:
    decrypt_message(bytes(tampered))
    print("ERROR: Tampered message was accepted!")
except Exception:
    print("SUCCESS: Tampered message was rejected!")