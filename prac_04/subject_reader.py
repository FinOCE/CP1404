"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = get_data()
    print_data_sentences(data)

def get_data():
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data

def print_data_sentences(data):
    for subject in data:
        print("{:4} is taught by {:12} and has {:3} students".format(subject[0], subject[1], subject[2]))

main()