numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]              3                                   Correct
numbers[-1]             2                                   Correct
numbers[3]              1                                   Correct
numbers[:-1]            [3, 1, 4, 1, 5, 9]                  Correct
numbers[3:4]            [1]                                 Correct
5 in numbers            True                                Correct
7 in numbers            False                               Correct
"3" in numbers          False                               Correct
numbers + [6, 5, 3]     [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]      Correct
"""

"""
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])
"""

# numbers[0] = "ten"
# numbers[-1] = 1
# numbers = numbers[2:]
# print(numbers)

VALUE = 9
value_exists = False
for i in range(0, len(numbers)):
    if numbers[i] == VALUE:
        value_exists = True
if value_exists == True:
    print(f"There is a {VALUE} in the array")