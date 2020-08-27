import math

def main():
    print("Welcome to sequences.py")

    val = get_values()
    choice = display_menu()

    while choice != 4:
        if choice == 1:
            get_even(val.x, val.y)
            choice = display_menu()
        elif choice == 2:
            get_odd(val.x, val.y)
            choice = display_menu()
        elif choice == 3:
            get_square(val.x, val.y)
            choice = display_menu()
        else:
            print("Invalid choice")
            choice = display_menu()
    
    print("Thank you for playing sequences.py")

def get_values():
    class val:
        x = int(input("X value: "))
        y = int(input("Y value: "))

    return val()

def get_even(x, y):
    for i in range(x, y+1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def get_odd(x, y):
    for i in range(x, y+1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def get_square(x, y):
    max_square = math.floor(y**0.5)
    for i in range(1, max_square+1):
        print(i*i, end=" ")
    print()

def display_menu():
    print()
    print("(1) Show the even numbers from x to y")
    print("(2) Show the odd numbers from x to y")
    print("(3) Show the squares from x to y")
    print("(4) Quit program")
    return int(input(">>> "))

main()