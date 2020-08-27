"""
program that would allow them to quickly work out the total price for a number of items, each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
The output should look something like (bold text represents user input):
"""

item_count = int(input("Number of items: "))

while item_count < 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))

total = 0

for i in range(0, item_count):
    item_price = float(input("Price of item: $"))

    while item_price < 0:
        print("Invalid item price!")
        item_price = float(input("Price of item: $"))
    
    total += item_price

print(f"Total price of {item_count} items is ${total:.2f}")