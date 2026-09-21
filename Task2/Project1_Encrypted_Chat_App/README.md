# 🔐 Project 1 — Encrypted Chat App

A Python-based encrypted chat application that demonstrates secure client-server communication using TCP sockets and AES-256-GCM authenticated encryption.

The project supports multiple clients, encrypted message transmission, TCP message framing, encrypted message logging, and basic error handling.

## 📌 Project Overview

This application uses a TCP client-server architecture.

Messages are encrypted on the client side using AES-256-GCM before being sent to the server. The server forwards the encrypted data to other connected clients, where the receiving client decrypts the message.

### Architecture

```
Client 1
   │
   │ AES-GCM encrypted message
   ▼
┌───────────────┐
│ Chat Server   │
│ TCP + Threads │
└───────┬───────┘
        │
        │ Encrypted data
        ▼
   Client 2
        │
        ▼
   AES-GCM Decryption
        │
        ▼
   Original Message
```

## ✨ Features

* Python TCP client/server communication
* AES-256-GCM authenticated encryption
* Pre-shared secret key
* Secure key storage using `.env`
* Multiple clients using Python threads
* Encrypted message broadcasting
* TCP message framing using a 4-byte length prefix
* Authentication tag and tamper detection
* Encrypted message logging
* Basic connection and error handling
* Clean and modular project structure

## 🔐 Security Concepts

### AES-256-GCM

AES-GCM is used for authenticated encryption.

It provides:

* **Confidentiality** — protects the message contents
* **Integrity** — detects unauthorized modification
* **Authentication** — verifies that the ciphertext has not been tampered with through the GCM authentication tag

### Pre-Shared Key

The same secret AES key is available to the communicating clients.

The key is generated randomly and stored in the `.env` file instead of being hard-coded directly into the Python source code.

### Nonce

A unique random nonce is generated for each encrypted message.

The nonce does not need to be secret, but it must not be reused with the same AES-GCM key.

### Tamper Detection

If encrypted data is modified, AES-GCM authentication fails and the message is rejected during decryption.

### TCP Message Framing

TCP provides a continuous byte stream rather than separate message boundaries.

This project uses a 4-byte length prefix before each encrypted message so the receiver knows how many bytes belong to one message.

### Encrypted Logging

The server stores encrypted message data in the log file rather than storing the plaintext message.

Base64 encoding is used to represent encrypted binary data as readable text for logging.

> Note: Base64 is an encoding method, not encryption. The actual protection is provided by AES-GCM.

## 📁 Project Structure

```
Project1_Encrypted_Chat_App/
│
├── server.py
├── client.py
├── crypto_utils.py
├── key_generator.py
├── requirements.txt
├── .env
├── .gitignore
│
└── logs/
    └── chat.log
```

## ⚙️ Requirements

* Python 3.x
* `cryptography`
* `python-dotenv`

## 📦 Installation

Install the required Python packages:

```
pip install -r requirements.txt
```

## 🔑 Generate the AES Key

Run:

```
python key_generator.py
```

The script generates a random 32-byte key, which provides an AES-256 key.

Store the generated key in `.env`:

```
CHAT_SECRET_KEY=YOUR_GENERATED_KEY
```

## ▶️ Running the Application

### 1. Start the server

```
python server.py
```

The server listens on:

```
127.0.0.1:5000
```

### 2. Start Client 1

Open another terminal and run:

```
python client.py
```

### 3. Start Client 2

Open another terminal and run:

```
python client.py
```

Multiple clients can connect to the server simultaneously.

### 4. Send messages

Type a message in one client.

The message is:

```
Plaintext
    ↓
AES-GCM Encryption
    ↓
Encrypted Data
    ↓
TCP
    ↓
Server
    ↓
Other Client
    ↓
AES-GCM Decryption
    ↓
Plaintext
```

Type:

```
exit
```

to close a client connection.

## 🧪 Testing

The project was tested for:

### Normal Encryption/Decryption

A plaintext message was encrypted and successfully decrypted back to the original message.

### Tamper Detection

An encrypted message was intentionally modified.

AES-GCM rejected the modified ciphertext, demonstrating integrity protection.

### Multiple Clients

Two clients were connected to the server simultaneously and successfully exchanged encrypted messages.

### TCP Message Framing

Messages were transmitted using a length-prefixed framing mechanism to ensure complete message boundaries over TCP.

### Encrypted Logging

Encrypted message data was stored in:

```
logs/chat.log
```

Plaintext chat messages were not stored in the log.

### Client Disconnect

Clients were tested using the `exit` command and the server handled client disconnections.

## 🛡️ Sensitive Data Protection

The `.env` file contains the secret encryption key and must never be uploaded to GitHub.

The `.gitignore` file excludes:

```
.env
__pycache__/
*.pyc
```

Never share the actual secret key publicly.

## ⚠️ Security Considerations

This project is an educational implementation and should not be considered a production-ready secure messaging application.

It uses a pre-shared key, meaning secure key distribution is assumed.

The application also does not implement:

* User authentication
* Public-key cryptography
* Perfect Forward Secrecy
* TLS
* Persistent user accounts
* End-to-end identity verification

These could be considered future improvements.

## 🚀 Future Improvements

Possible future improvements include:

* User authentication
* Secure key exchange
* TLS-based transport security
* Public-key cryptography
* Better connection management
* Private messaging
* Usernames
* Improved logging and monitoring

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

* Python socket programming
* TCP client-server communication
* AES-GCM authenticated encryption
* Cryptographic key management
* Nonces and authentication tags
* TCP message framing
* Python threading
* Secure handling of environment variables
* Encrypted logging
* Basic cybersecurity testing

## 👨‍💻 Project

**Project:** Encrypted Chat App
**Task:** SyntexHub Cybersecurity Internship — Task 2
**Technology:** Python
**Encryption:** AES-256-GCM
**Network Protocol:** TCP
