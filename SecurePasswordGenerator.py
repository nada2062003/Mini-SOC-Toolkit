import secrets
import string
import hashlib
import os


def run_password_generator():

    print("\n" + "=" * 50)
    print("        SECURE PASSWORD GENERATOR")
    print("=" * 50)

    PASSWORD_LENGTH = 8
    HASH_FILE = "generated_hashes.txt"

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + numbers + symbols

    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_used_hashes():
        if not os.path.exists(HASH_FILE):
            return set()

        with open(HASH_FILE, "r") as file:
            return set(line.strip() for line in file)

    def save_hash(password_hash):
        with open(HASH_FILE, "a") as file:
            file.write(password_hash + "\n")

    used_hashes = load_used_hashes()

    while True:
        try:
            count = int(input("\nHow many passwords do you want?: "))

            if count > 0:
                break

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    print("\nGenerated Passwords:\n")

    for i in range(count):

        while True:

            password_characters = [
                secrets.choice(lowercase),
                secrets.choice(uppercase),
                secrets.choice(numbers),
                secrets.choice(symbols)
            ]

            for j in range(PASSWORD_LENGTH - 4):
                password_characters.append(
                    secrets.choice(all_characters)
                )

            secrets.SystemRandom().shuffle(password_characters)

            password = "".join(password_characters)
            password_hash = hash_password(password)

            if password_hash not in used_hashes:

                used_hashes.add(password_hash)
                save_hash(password_hash)

                print(f"{i + 1}. {password}")
                break

    print("\nSecurity Features:")
    print("✓ Password length = 8")
    print("✓ Uppercase letter")
    print("✓ Lowercase letter")
    print("✓ Number")
    print("✓ Special character")
    print("✓ Secure random generation")
    print("✓ Duplicate password prevention")
    print("✓ SHA-256 password history")