import socket
import threading
import struct

from crypto_utils import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 5000


def receive_message():
    header = client.recv(4)

    if not header:
        return None

    message_length = struct.unpack("!I", header)[0]

    data = b""

    while len(data) < message_length:
        chunk = client.recv(message_length - len(data))

        if not chunk:
            return None

        data += chunk

    return data


def send_message(data):
    header = struct.pack("!I", len(data))
    client.sendall(header + data)


def receive_messages():
    while True:
        try:
            encrypted_data = receive_message()

            if encrypted_data is None:
                break

            message = decrypt_message(encrypted_data)

            print(f"\nMessage: {message}")

        except Exception:
            print("Connection closed.")
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

print("Connected to encrypted chat server.")

receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()


while True:
    message = input()

    if message.lower() == "exit":
        break

    encrypted_data = encrypt_message(message)

    send_message(encrypted_data)


client.close()