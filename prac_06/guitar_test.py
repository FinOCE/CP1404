from guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16045.40)
    another = Guitar("Another Guitar", 2013, 10904.75)

    print(f"{gibson.name} get_age() - Expected 98. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 7. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

main()