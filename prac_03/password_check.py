MIN_LENGTH = 3

def main():
    password = get_password()
    print(convert_to_asterisk(password))

def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long")
        password = input("Enter password: ")
    
    return password

def convert_to_asterisk(password):
    new_password = len(password) * "*"
    return new_password

main()