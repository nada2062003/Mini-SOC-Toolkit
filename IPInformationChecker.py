import ipaddress


def run_ip_checker():

    print("\n" + "=" * 50)
    print("          IP INFORMATION CHECKER")
    print("=" * 50)

    ip_input = input("\nEnter an IP address: ").strip()

    try:
        ip = ipaddress.ip_address(ip_input)

        print("\nIP Analysis")
        print("-" * 35)

        print("IP Address:", ip)
        print("IP Version:", ip.version)

        if ip.is_private:
            print("Type: Private IP")
        else:
            print("Type: Public IP")

        print("Loopback:", "Yes" if ip.is_loopback else "No")
        print("Multicast:", "Yes" if ip.is_multicast else "No")
        print("Reserved:", "Yes" if ip.is_reserved else "No")

        print("\nStatus: Valid IP Address")

    except ValueError:
        print("\nERROR: Invalid IP Address")