# TCP Port Scanner

A simple Python-based TCP Port Scanner developed as part of the **SyntexHub Cybersecurity Internship**.

## Project Overview

This tool scans a specified range of TCP ports on a target IP address or hostname and identifies whether ports are **open or closed**.

The scanner uses **multithreading** to scan multiple ports efficiently.

## Features

- Scan a custom TCP port range
- Accept IP address or hostname
- Detect open and closed ports
- Uses TCP socket connections
- Multithreaded scanning with `ThreadPoolExecutor`
- Handles invalid input, timeouts, and socket errors
- Displays a summary of open ports

## Technologies Used

- Python
- Socket Programming
- TCP/IP
- ThreadPoolExecutor

## Project Structure

    Task1_Port_Scanner/
    ├── port_scanner.py
    ├── port_scanner_output.png
    └── README.md

## How to Run

Run the program from the terminal:

    python port_scanner.py

Enter the target IP/hostname and the starting and ending ports when prompted.

### Example

    Enter target IP/hostname: 127.0.0.1
    Enter starting port: 7995
    Enter ending port: 8005

### Sample Result

    Target: 127.0.0.1 (127.0.0.1)
    Scanning ports 7995-8005...

    [OPEN] Port 8000

    Scan completed.
    Open ports: [8000]

## Testing

The scanner was tested on the local machine using:

    Target: 127.0.0.1
    Port Range: 7995-8005

Port **8000** was detected as open using a temporary local HTTP server.

## Security Note

This tool should only be used to scan systems and networks that you own or have explicit permission to test.

## Internship

This project was completed as part of the **SyntexHub Cybersecurity Internship**.

## Author

Cybersecurity Intern
