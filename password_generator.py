
# Task 4: Password Generator

import random
import string


def generate_password(length):
    """Generate a random password using letters, digits, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def main():
    print("=" * 35)
    print("       PASSWORD GENERATOR")
    print("=" * 35)

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Error: Password length must be at least 4.")
            return

        password = generate_password(length)
        print("\nPassword generated successfully!")
        print("Your password:", password)

    except ValueError:
        print("Error: Please enter a valid whole number.")


if __name__ == "__main__":
    main()
