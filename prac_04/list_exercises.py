""" task 1 """
COUNT = 5

def main():
    numbers = get_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[COUNT - 1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    mean = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {mean:.1f}")

def get_numbers():
    numbers = []
    for _ in range(0, COUNT):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers

main()

""" task 2 """
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
def main():
    user = input("Enter username: ")
    print(attempt_login(user))

def attempt_login(user):
    for username in usernames:
        if user == username:
            return "Access granted"
    return "Access denied"

main()