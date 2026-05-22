import random 
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = r"!@#$%^&*()-+"
numbers = "1234567890"

def main():
    while True:
        try:
            length = int(input("Enter the length of your password or enter 99 to exit: "))
            if length == 99:
                break
            password = generate_password(length)
            print(f"Your password is {password}")
        except ValueError:
            print("Enter a number")

def generate_password(length):
    password = []
    for i in range(length):
        data_type = random.randint(1, 4)
        if data_type == 1:
            char = random.choice(lowercase)
            password.append(char)
        if data_type == 2:
            char = random.choice(uppercase)
            password.append(char)
        if data_type == 3:
            char = random.choice(symbols)
            password.append(char)
        if data_type == 4:
            char = random.choice(numbers)
            password.append(char)
    random.shuffle(password)
    password = "".join(password)
    return password
if __name__ == "__main__":
    main()