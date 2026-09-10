import json
import os
import base64
import hashlib
import getpass
from cryptography.fernet import Fernet, InvalidToken


DATA_FILE = "passwords.json"
SALT_FILE = "salt.bin"


def create_key(master_password):
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as file:
            file.write(salt)
    else:
        with open(SALT_FILE, "rb") as file:
            salt = file.read()

    key = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode(),
        salt,
        100_000,
        32
    )

    return base64.urlsafe_b64encode(key)


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()

    return encrypted_data


def save_data(data, key):
    encrypted_data = Fernet(key).encrypt(
        json.dumps(data).encode()
    )

    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)


def decrypt_data(key):
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = Fernet(key).decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    except InvalidToken:
        print("\nInvalid master password or corrupted data.")
        return None


def add_password(data, key):
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ")

    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data, key)
    print("\nPassword saved successfully.")


def retrieve_password(data):
    website = input("Enter website: ").strip()

    if website in data:
        print("\nUsername:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("\nNo entry found.")


def search_password(data):
    search = input("Enter search term: ").lower()

    results = [
        website for website in data
        if search in website.lower()
    ]

    if results:
        print("\nMatching entries:")
        for website in results:
            print("-", website)
    else:
        print("\nNo matching entries found.")


def delete_password(data, key):
    website = input("Enter website: ").strip()

    if website in data:
        del data[website]
        save_data(data, key)
        print("\nEntry deleted successfully.")
    else:
        print("\nNo entry found.")


def main():
    print("=" * 35)
    print("       PASSWORD MANAGER")
    print("=" * 35)

    master_password = getpass.getpass("Enter master password: ")

    key = create_key(master_password)
    data = decrypt_data(key)

    if data is None:
        return

    while True:
        print("\n===== Menu =====")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_password(data, key)

        elif choice == "2":
            retrieve_password(data)

        elif choice == "3":
            search_password(data)

        elif choice == "4":
            delete_password(data, key)

        elif choice == "5":
            print("\nExiting Password Manager...")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()