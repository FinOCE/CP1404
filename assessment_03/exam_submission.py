"""
CP1401 2020-2 Final Exam - Online Assignment
Name: Finley Sherwood
"""

# 1.
# Explanation: The function uses the variable "counter" without defining it, and only changes the value of the variable "counter" that is local to the function.

# Solution:
counter = 0

def increment(counter):
    counter += 1
    return counter

counter = increment(counter)

# 3.
gene1 = 'ggg'
gene2 = 'ttt'
dna = (gene1 + gene2) * 2

# 5.
def student_info(age, country="France"):
    print("Age: {} Country: {}".format(age, country))

student_info(20, 'Belgium')
student_info(24)

# 6. 
dna = list("acgtaact")

nucleotides = []
for nucleotide in dna:
    if nucleotide not in [nucleotide[0] for nucleotide in nucleotides]:
        nucleotides.append([nucleotide, 1])
    else:
        for i in range(len(nucleotides)):
            if nucleotides[i][0] == nucleotide:
                nucleotides[i] = [nucleotide, nucleotides[i][1] + 1]
nucleotides = sorted(nucleotides, key=lambda x: x[1])

for nucleotide in nucleotides:
    print(f'Frequency of {nucleotide[0]} is {nucleotide[1]}')

# 8.
location = [34, [4.5, 12, [45, 6.7, 'ship']], 'wreck']

print(location[1][2][2][1])

# 9.
MIN_PRICE = 0
MAX_PRICE = 3
NUMBER_OF_APPLES = 10

while True:
    cost = input('Cost of an apple: ')
    try:
        cost = float(cost)
        if cost > MIN_PRICE and cost < MAX_PRICE:
            break
        else:
            print(f'Cost must be between {MIN_PRICE} and {MAX_PRICE}')
    except ValueError:
        print('Invalid input')

print(f'Cost of {NUMBER_OF_APPLES} apples is ${cost*NUMBER_OF_APPLES:.2f}')

# 11.
class Car():
    def __init__(self, speed=30):
        self.speed = speed

class SportsCar(Car):
    def print_speed(self):
        print(f"Sport Car Speed : {self.speed*10}")

class PickupCar(Car):
    def __init__(self, speed=30, load=2):
        super().__init__(speed)
        self.load = load
    
    def print_speed(self):
        print(f"Pick-up Car Speed : {self.speed - self.load}")

SportsCar().print_speed()
PickupCar().print_speed()

# Explanation: I refactored the code by creating new classes for the two types of cars, and made only the PickupCar include the load argument, since the SportsCar or regular Car classes don't seem to require that attribute. The code is better in this version because it means each type of car can have individual attributes set to it, they can be defined as either type when created, don't need to pass through extra arguments when running functions like print_speed(), and allow for more types of cars to be added easily.

# 12. 
# Explanation: The programmer intends to create a patten of six zeros, then add a one after every two zeros. [0, 0, 0, 0, 0 , 0] -> [0, 0, 1, 0, 0, 1, 0, 0, 1]

# Solution:
pattern = 6 * [0]

for i in range(len(pattern) + 3):
    if i % 3 == 2:
        pattern = pattern[:i] + [1] + pattern[i:]

print(pattern)

# 13.
movie = "The man who knew too much"

# a.
print(" ".join(movie.split(' ')[0:2]))

# b.
print(" ".join(movie.split(' ')[2:6]))

# c.
print(movie.split(' ')[3])

# d.
print(movie[::-1])

# e.
print(f"The movie name has {len(movie.split(' '))} words")

# f.
print(f"The movie name has {len(movie)} characters")

# 14.
def count_digits(number):
    # In the collab room, Iti said we could add code before the return so its not so messy
    even_numbers_count = len([1 for num in number if num != '.' and int(num) % 2 == 0])
    odd_numbers_count = len([1 for num in number if num != '.' and int(num) % 2 == 1])
    zeros_before_decimaL_count = len([1 for num in number.split('.')[0] if int(num) == 0])
    return (even_numbers_count, odd_numbers_count, zeros_before_decimaL_count)

number = input("Enter a number ")
print(count_digits(number))

# 16.
# Explanation: FileNotFoundError occurs when a file is tried to be opened when it doesn't exist. To prevent this, the code can be nested in a "try: ... except FileNotFoundError ..." so the program doesn't crash

# Solution:
try:
    file = open('file.txt')
except FileNotFoundError:
    print('File not found')

# 17.
primes = [11, 17, 3, 7, 19, 2, 5, 23, 13]
not_primes = [number for number in range(25) if number not in primes]
primes_sorted = [number**2 for number in sorted(primes)]

# 18.
series = [1, 1]

[series.append(series[i] + series[i+1]) for i in range(8)]

# 19.
# Answered in bloggers.py

# 21.
# Answered in jungle.py