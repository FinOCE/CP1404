import random

def main():
    score_count = get_score_count()

    file = open("results.txt", "w")

    for _ in range(0, score_count):
        random_score = random.randint(0, 100)
        line = f"{random_score} is {determine_result(random_score)}\n"
        file.write(line)
    
    file.close()

def get_score_count():
    score = int(input("Enter amount of scores: "))

    while score < 0 or score > 100:
        print("Invalid score entered. Please try again.")
        score = float(input("Enter amount of scores: "))

    return score

def determine_result(score):
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"

main()