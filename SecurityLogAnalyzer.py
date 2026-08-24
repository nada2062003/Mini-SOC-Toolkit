import re
import os


def run_log_analyzer():

    print("\n" + "=" * 50)
    print("          SECURITY LOG ANALYZER")
    print("=" * 50)

    log_file = input("\nEnter log file name: ").strip()

    if not os.path.exists(log_file):
        print("\nError: Log file does not exist.")
        return

    alert_threshold = 3
    failed_logins = {}

    with open(log_file, "r", encoding="utf-8") as file:

        for line in file:

            if "Failed login" in line:

                ip_match = re.search(
                    r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
                    line
                )

                if ip_match:

                    ip_address = ip_match.group()

                    if ip_address in failed_logins:
                        failed_logins[ip_address] += 1
                    else:
                        failed_logins[ip_address] = 1

    print("\nAnalysis Results")
    print("-" * 40)

    if not failed_logins:
        print("No failed login attempts detected.")
        return

    for ip, attempts in failed_logins.items():

        if attempts >= 5:
            risk_level = "HIGH"

        elif attempts >= alert_threshold:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"

        print(f"\nIP Address: {ip}")
        print(f"Failed Attempts: {attempts}")
        print(f"Risk Level: {risk_level}")

        if attempts >= alert_threshold:
            print("ALERT: Possible Brute Force Attack!")

        print("-" * 40)