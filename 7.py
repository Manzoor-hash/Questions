import random
import string

def password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Password length should be a positive integer.")
    else:
        Password = password(length)
        print("Generated password:", Password)

if __name__ == "__main__":
    main()