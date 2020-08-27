"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

while score < 0 or score > 100:
    print("Invalid score entered. Please try again.")
    score = float(input("Enter score: "))

if score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
elif score <= 100:
    print("Excellent")
"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""