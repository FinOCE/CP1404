import random

def main():
    score = get_score()
    print(determine_result(score))

    random_score = random.randint(0, 100)
    print(f"The random score of {random_score} is {determine_result(random_score)}")

def get_score():
    score = float(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score entered. Please try again.")
        score = float(input("Enter score: "))

    return score

def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()