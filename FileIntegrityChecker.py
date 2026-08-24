import hashlib
import os


def run_file_integrity_checker():

    print("\n" + "=" * 50)
    print("          FILE INTEGRITY CHECKER")
    print("=" * 50)

    file_path = input("\nEnter the file path to check: ").strip()

    if not os.path.exists(file_path):
        print("\nError: File does not exist.")
        return

    def calculate_hash(path):

        sha256 = hashlib.sha256()

        with open(path, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    current_hash = calculate_hash(file_path)

    # Create a different baseline file for each monitored file
    safe_name = os.path.basename(file_path).replace(".", "_")
    hash_file = f"{safe_name}_hash.txt"

    if not os.path.exists(hash_file):

        with open(hash_file, "w") as file:
            file.write(current_hash)

        print("\nBaseline created successfully.")
        print("File:", file_path)
        print("Status: SECURE")

    else:

        with open(hash_file, "r") as file:
            previous_hash = file.read().strip()

        if current_hash == previous_hash:

            print("\nFile:", file_path)
            print("Status: NO CHANGES DETECTED")

        else:

            print("\n" + "!" * 50)
            print("              SECURITY ALERT")
            print("!" * 50)

            print("\nFile:", file_path)
            print("Status: FILE HAS BEEN MODIFIED!")

            print("\nPrevious SHA-256:")
            print(previous_hash)

            print("\nCurrent SHA-256:")
            print(current_hash)