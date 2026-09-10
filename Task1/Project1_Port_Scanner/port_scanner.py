import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
                return port, "OPEN"
            else:
                print(f"[CLOSED] Port {port}")
                return port, "CLOSED"

    except socket.timeout:
        print(f"[TIMEOUT] Port {port}")
        return port, "TIMEOUT"

    except socket.error as e:
        print(f"[ERROR] Port {port}: {e}")
        return port, "ERROR"


def main():
    print("=" * 40)
    print("        TCP PORT SCANNER")
    print("=" * 40)

    target = input("Enter target IP/hostname: ").strip()

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        if not (1 <= start_port <= end_port <= 65535):
            print("Invalid port range.")
            return

        target_ip = socket.gethostbyname(target)

        print(f"\nTarget: {target} ({target_ip})")
        print(f"Scanning ports {start_port}-{end_port}...\n")

        with ThreadPoolExecutor(max_workers=50) as executor:
            results = list(
                executor.map(
                    lambda port: scan_port(target_ip, port),
                    range(start_port, end_port + 1)
                )
            )

        open_ports = [port for port, status in results if status == "OPEN"]

        print("\n" + "=" * 40)
        print("Scan completed.")
        print(f"Open ports: {open_ports}")
        print("=" * 40)

    except ValueError:
        print("Please enter valid numbers for ports.")

    except socket.gaierror:
        print("Invalid hostname or IP address.")


if __name__ == "__main__":
    main()