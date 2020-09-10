emails = {}

def main():
    email = input("Email: ")
    while email != "":
        if "@" in email:
            if email not in emails:
                email = email.split("@")
                add_new_email(email[0], email[1])
            else:
                print("Email already in system.")
        else:
            print("Invalid email. Please try again.")
        email = input("Email: ")
    
    print_emails()

def add_new_email(name, domain):
    full_email = name + "@" + domain
    full_name = name.replace(".", " ").title()

    name_checker = input(f"Is your name {full_name}? (Y/n) ")
    if "n" in name_checker.lower():
        full_name = input("Name: ").title()
    
    emails[full_email] = full_name

def print_emails():
    for email in emails:
        print(f"{emails[email]} ({email})")

main()