import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from dotenv import load_dotenv

load_dotenv()

key = base64.b64decode(os.getenv("CHAT_SECRET_KEY"))

aes = AESGCM(key)


def encrypt_message(message):
    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    return nonce + ciphertext


def decrypt_message(encrypted_data):
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()