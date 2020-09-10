# I assume formatting the dictionary in this way is ok. I create objects this way in JavaScript.
COLOURS = {
    "AliceBlue": "#f0f8ff",
    "Beige": "#f5f5dc",
    "Black": "#ffffff",
    "BlueViolet": "#8a2be2",
    "Coral": "#ff7f50",
    "DarkGreen": "#006400",
    "Gold1": "#ffd700",
    "Gray": "#bebebe",
    "HotPink": "#ff69b4",
    "Magenta": "#ff00ff"
}

for colour in COLOURS:
    max_length = max([len(colour) for colour in COLOURS])
    print(f"The hex code for {colour:{max_length}} is {COLOURS[colour]}")

colour_name = input("Enter colour name: ")
while colour_name != "":
    valid = False
    for colour in COLOURS:
        if colour_name.upper() == colour.upper():
            print(COLOURS[colour])
            valid = True
    if valid == False:
        print("That is not a valid colour. Please try again.")
    colour_name = input("Enter colour name: ")

print("Exiting program")