import socket
import threading
import struct
import logging
import base64

HOST = "127.0.0.1"
PORT = 5000

logging.basicConfig(
    filename="logs/chat.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

clients = []


def receive_message(conn):
    header = conn.recv(4)

    if not header:
        return None

    message_length = struct.unpack("!I", header)[0]

    data = b""

    while len(data) < message_length:
        chunk = conn.recv(message_length - len(data))

        if not chunk:
            return None

        data += chunk

    return data


def send_message(conn, data):
    header = struct.pack("!I", len(data))
    conn.sendall(header + data)


def broadcast(encrypted_data, sender_conn):
    for client in clients[:]:
        if client != sender_conn:
            try:
                send_message(client, encrypted_data)
            except:
                if client in clients:
                    clients.remove(client)


def handle_client(conn, address):
    print(f"Client connected: {address}")

    clients.append(conn)

    try:
        while True:
            encrypted_data = receive_message(conn)

            if encrypted_data is None:
                break


            print(f"Encrypted message received from {address}")

            logging.info(
    f"Encrypted message from {address}: "
    f"{base64.b64encode(encrypted_data).decode()}"
)


            broadcast(encrypted_data, conn)

    except Exception as e:
        print(f"Error with {address}: {e}")

    finally:
        if conn in clients:
            clients.remove(conn)

        conn.close()

        print(f"Client disconnected: {address}")
       
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print(f"Encrypted chat server listening on {HOST}:{PORT}")

while True:
    conn, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, address)
    )

    thread.start()