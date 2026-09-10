# Password Manager

A Python-based local password manager that securely stores credentials using encryption.

## 📌 Project Overview

This project is a simple local password manager developed as part of the SyntexHub Cybersecurity Internship.

It allows users to securely add, retrieve, search, and delete stored credentials. The credentials are encrypted before being saved to local storage.

## ✨ Features

- Master password authentication
- Add credentials
- Retrieve saved credentials
- Search credentials by website
- Delete credentials
- Encrypted local storage
- Secure password input using `getpass`

## 🔐 Security

- Credentials are encrypted before being stored.
- A master password is used to derive the encryption key.
- Passwords are not stored as plain text.
- Test credentials were used during demonstration.

## 🛠️ Technologies Used

- Python
- `cryptography`
- JSON
- `hashlib`
- `getpass`

## 📂 Project Structure

    Project2_Password_Manager/
    ├── password_manager.py
    ├── password_manager_output_1.png
    └── password_manager_output_2.png

> `passwords.json` and `salt.bin` are generated locally during execution and should not be uploaded to GitHub.

## ▶️ How to Run

Install the required library:

    pip install cryptography

Run the program:

    python password_manager.py

Enter a master password when prompted and use the menu to manage credentials.

## 🧪 Demonstrated Operations

The project was tested successfully for:

1. Adding a credential
2. Retrieving a credential
3. Searching for a credential
4. Deleting a credential
5. Verifying that the deleted credential is no longer available

## 📸 Output

The project output is demonstrated in:

- `password_manager_output_1.png`
- `password_manager_output_2.png`

## 🎯 Learning Outcomes

Through this project, I practiced:

- Python file handling
- JSON data storage
- Password management concepts
- Encryption and decryption
- Secure password input
- Exception handling
- Basic cybersecurity principles

## ⚠️ Disclaimer

This project was developed for educational purposes as part of a cybersecurity internship. It is intended for local testing and learning and should not be considered a production-ready password manager.