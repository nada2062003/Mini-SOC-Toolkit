from PasswordStrengthChecker import run_password_checker
from SecurePasswordGenerator import run_password_generator
from FileIntegrityChecker import run_file_integrity_checker
from SecurityLogAnalyzer import run_log_analyzer
from NetworkPortScanner import run_port_scanner
from IPInformationChecker import run_ip_checker
from PhisherURLAnalyzer import run_phishing_analyzer

print("=" * 55)
print("                 MINI SOC TOOLKIT")
print("=" * 55)

while True:

    print("\n[1] Password Strength Checker")
    print("[2] Secure Password Generator")
    print("[3] File Integrity Checker")
    print("[4] Security Log Analyzer")
    print("[5] Network Port Scanner")
    print("[6] IP Information Checker")
    print("[7] Phishing URL Analyzer")
    print("[0] Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        run_password_checker()


    elif choice == "2":
        run_password_generator()


    elif choice == "3":
        run_file_integrity_checker()


    elif choice == "4":
        run_log_analyzer()


    elif choice == "5":
        run_port_scanner()


    elif choice == "6":
        run_ip_checker()


    elif choice == "7":
        run_phishing_analyzer()


    elif choice == "0":
        print("\n" + "=" * 60)
        print("              MINI SOC TOOLKIT CLOSED")
        print("=" * 60)
        print("Thank you for using Mini SOC Toolkit.")
        break


    else:
        print("\n[ERROR] Invalid option.")
        print("Please select a number from 0 to 7.")
    input("\nPress Enter to return to the main menu...")
