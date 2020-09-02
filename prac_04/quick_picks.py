import random

RANDOM_NUMBER_COUNT = 6
MIN_VALUE = 1
MAX_VALUE = 45

def main():
    line_count = int(input("How many quick picks? "))
    print_lines(line_count)

def print_lines(line_count):
    for _ in range(0, line_count):
        line_values = []
        for _ in range(0, RANDOM_NUMBER_COUNT):
            value = random.randint(MIN_VALUE, MAX_VALUE)
            while value in line_values:
                value = random.randint(MIN_VALUE, MAX_VALUE)
            print(f"{value:2}", end=" ")
        print()

main()