import random
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def main():
    try:
        length = int(input("Password lenght: ").strip())
    except ValueError:
        print("The lenght must be an integer!")
        return 0
    else:
        if length < 4 or length > 100:
            print("The lenght must be between 4 and 100!")
            return 0
        password = generate_password(length)
        with open("log.txt", "a") as file:
            file.write(f"{len(password)}: {password}\n")
        print("Password:", password)
        return 1

def generate_password(length):
    password = []
    parts = (ascii_uppercase, ascii_lowercase, digits, punctuation)
    for time in range(length):
        index = time % len(parts)
        password.append(random.choice(parts[index]))
    random.shuffle(password)
    return "".join(password)

main()