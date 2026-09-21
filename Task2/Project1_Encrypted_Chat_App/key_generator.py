import secrets
import base64

key = secrets.token_bytes(32)

encoded_key = base64.b64encode(key).decode()

print("Generated AES-256 key:")
print(encoded_key)