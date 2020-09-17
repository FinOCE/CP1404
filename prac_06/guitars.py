from guitar import Guitar

guitars = []

def main():
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        while True:
            try:
                year = int(input("Year: "))
                break
            except ValueError:
                print("Invalid year, please try again.")
        while True:
            try:
                cost = float(input("Cost: $"))
                break
            except ValueError:
                print("Invalid cost, please try again.")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("\nName: ")
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        is_vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth $ {guitar.cost:,.2f}{is_vintage}")

main()