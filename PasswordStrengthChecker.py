def run_password_checker():

    print("\n" + "=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("\nEnter your password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    if any(char in special_characters for char in password):
        score += 1

    print("\nPassword Security Report")
    print("-" * 30)

    if score <= 2:
        print("Strength: WEAK")

    elif score <= 4:
        print("Strength: MEDIUM")

    else:
        print("Strength: STRONG")

    print("Score:", score, "/ 5")