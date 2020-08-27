name = input("Enter name: ")

# 1
file = open("{}.txt".format(name), "w")
file.write("{}\n".format(name))
file.close()

# 2
file = open("{}.txt".format(name), "r")
user = file.readline()
print("Your name is {}".format(user))
file.close()

# 3
file = open("numbers.txt", "r")
lines = file.readlines()
total = int(lines[0]) + int(lines[1])
print(total)
file.close()

# 4
file = open("numbers.txt", "r")
lines = file.readlines()
total = 0
for i in range(0, len(lines)):
    total += int(lines[i])
print(total)
file.close()