import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

# Example usage:
password_length = int(input("Enter the desired password length: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

passwords = generate_multiple_passwords(num_passwords, password_length)

print("\nGenerated Passwords:")
for index, password in enumerate(passwords, start=1):
    print(f"Password {index}: {password}")