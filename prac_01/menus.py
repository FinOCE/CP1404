"""
Supplied pseudocode:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

def main():
    name = input("Enter name: ")

    choice = display_menu()

    while choice != "q":
        if choice == "h":
            print(f"Hello {name}")
            choice = display_menu()
        elif choice == "g":
            print(f"Goodbye {name}")
            choice = display_menu()
        else:
            print("Invalid choice")
            choice = display_menu()
    
    print("Finished.")

def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    return input(">>> ").lower()

main()