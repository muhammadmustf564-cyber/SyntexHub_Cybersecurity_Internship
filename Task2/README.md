# 🔐 Task 2 — Encrypted Chat App

This task focuses on building a secure multi-client chat application using Python, TCP sockets, and AES-256-GCM authenticated encryption.

## 📌 Task Overview

The project demonstrates encrypted client-server communication where messages are encrypted before transmission and decrypted only by the receiving client.

### Project Completed

* **Project 1 — Encrypted Chat App** ✅

## 🔐 Project 1 — Encrypted Chat App

A Python-based encrypted chat application supporting multiple clients through a TCP server.

### Key Features

* Python TCP client/server communication
* AES-256-GCM authenticated encryption
* Pre-shared secret key
* Secure key storage using `.env`
* Multiple clients using threading
* Encrypted message broadcasting
* TCP message framing
* Tamper detection
* Encrypted message logging
* Basic error handling

### Message Flow

```
Client 1
   ↓
AES-GCM Encryption
   ↓
Encrypted Data
   ↓
TCP Server
   ↓
Encrypted Data Forwarded
   ↓
Client 2
   ↓
AES-GCM Decryption
   ↓
Original Message
```

## 🛡️ Security Concepts Practiced

* Confidentiality
* Integrity
* Authentication tags
* AES-256-GCM
* Nonces
* Pre-shared keys
* Environment variable protection
* Secure handling of sensitive data
* TCP message framing
* Encrypted logging

## 🧪 Testing

The application was tested for:

* Successful encryption and decryption
* AES-GCM tamper detection
* Multiple client connections
* Encrypted message exchange
* TCP message framing
* Encrypted logging
* Client disconnection handling

## 📁 Project Structure

```
Task2_Encrypted_Chat_App/
│
├── README.md
│
└── Project1_Encrypted_Chat_App/
    ├── README.md
    ├── server.py
    ├── client.py
    ├── crypto_utils.py
    ├── key_generator.py
    ├── test_crypto.py
    ├── requirements.txt
    ├── .gitignore
    └── logs/
        └── chat.log
```

## 🎓 Learning Outcome

This task provided practical experience with Python networking, authenticated encryption, cryptographic key handling, multithreading, TCP communication, message framing, encrypted logging, and basic cybersecurity testing.

---

**Task:** SyntexHub Cybersecurity Internship — Task 2
**Project:** Encrypted Chat App
**Technology:** Python
**Encryption:** AES-256-GCM
**Protocol:** TCP

