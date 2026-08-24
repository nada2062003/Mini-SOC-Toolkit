import socket
from datetime import datetime


def run_port_scanner():

    print("\n" + "=" * 50)
    print("            NETWORK PORT SCANNER")
    print("=" * 50)

    target = input("\nEnter target IP address: ").strip()

    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3306: "MySQL",
        3389: "RDP",
        8080: "HTTP-ALT"
    }

    print("\nTarget:", target)
    print("Scan Started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 50)

    open_ports = []

    for port, service in ports.items():

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)

        try:
            result = scanner.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN]   Port {port:<5} - {service}")
                open_ports.append((port, service))

            else:
                print(f"[CLOSED] Port {port:<5} - {service}")

        except socket.gaierror:
            print("\nError: Invalid hostname or IP address.")
            scanner.close()
            return

        except socket.error:
            print("\nError: Could not connect to target.")
            scanner.close()
            return

        scanner.close()

    print("\n" + "-" * 50)
    print("Scan Summary")
    print("-" * 50)

    if open_ports:

        print(f"Open Ports Found: {len(open_ports)}\n")

        for port, service in open_ports:
            print(f"Port {port} - {service}")

    else:
        print("No open ports found.")

    print("\nScan completed successfully.")