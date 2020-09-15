"""
Name: Finley Sherwood
Date started: 03/09/2020
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-1-FinOCE
"""

LIST_FILE_NAME = "places.csv"

def main():
    """ main function """
    print("Travel Tracker 1.0 - by Finley Sherwood")
    list = open(LIST_FILE_NAME)
    lines = list_to_array(list)
    print("{} places loaded from {}".format(len(lines), LIST_FILE_NAME))

    method = get_menu()
    while method != "Q":
        if method == "L":
            list_method(lines)
        elif method == "A":
            lines = add_method(lines)
        elif method == "M":
            lines = mark_method(lines)
        else:
            print("Invalid menu choice")
        method = get_menu()
    quit_method(lines)

def list_to_array(list):
    """ converts .csv file to array """
    lines_raw = [line for line in list] # separates the file's lines into individual elements of an array
    lines = []
    for line in lines_raw:
        line_content = line.strip().split(',')
        line_content[2] = int(line_content[2])
        lines.append(line_content)
    lines = sort_by_visited(lines)
    return lines

def sort_by_visited(lines):
    """ sort the visited and not visited locations by priority, then combine and set as variable lines """
    lines_visited = []
    lines_not_visited = []
    for line in lines:
        if line[3] == "v":
            lines_visited.append(line)
        else:
            lines_not_visited.append(line)
    lines_visited.sort(key=sort_by_priority)
    lines_not_visited.sort(key=sort_by_priority)
    lines = lines_not_visited + lines_visited
    return lines

def sort_by_priority(line):
    """ used in sort functions above to sort by priority """
    return line[2]

def get_menu():
    """ print menu text and request method response """
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    method = input(">>> ").upper()
    return method

def list_method(lines):
    """ lists locations and their relative information """
    max_string_length = get_max_string_length(lines)
    not_visited_counter = 0
    for i in range(0, len(lines)):
        parts = lines[i]
        if parts[3] == "v":
            visited = " "
        else:
            visited = "*"
            not_visited_counter += 1
        
        counter = f"{i+1:{max_string_length[0]}}"
        city = f"{parts[0]:{max_string_length[1]}}"
        country = f"{parts[1]:{max_string_length[2]}}"
        priority = f"{parts[2]:{max_string_length[3]}}"
        
        print(f"{visited}{counter}. {city} in {country} priority {priority}")
    if not_visited_counter > 0:
        not_visited_message = f"You still want to visit {not_visited_counter} places."
    else:
        not_visited_message = "No places left to visit. Why not add a new place?"
    print(f"{len(lines)} places. {not_visited_message}")

def get_max_string_length(lines):
    """ returns array with the max length of each element """
    counter = len(str(len(lines)))
    cities = len(max([line[0] for line in lines], key=len))
    countries = len(max([line[1] for line in lines], key=len))
    priority = len(str(max([line[2] for line in lines])))
    
    max_string_length = [counter, cities, countries, priority]
    return max_string_length

def add_method(lines):
    """ adds a location to the program """
    name = get_valid_input("Name: ")
    country = get_valid_input("Country: ")
    priority = get_valid_number("Priority: ")

    lines.append([name, country, int(priority), "n"]) # add elements to lines array
    print(f"{name} in {country} (priority {priority}) added to Travel Checker")

    lines = sort_by_visited(lines)
    return lines

def get_valid_input(question):
    """ checks if string input is valid, if not requests again """
    response = input(question)
    while response == "":
        print("Input can not be blank")
        response = input(question)
    return response

def get_valid_number(question):
    """ checks if number input is valid, if not requests again """
    response = input(question)
    test_number_response = test_number_add(response)
    while test_number_response != True:
        print(test_number_response)
        response = input(question)
        test_number_response = test_number_add(response)
    return response

def test_number_add(value):
    """ determines if the integar is valid """
    try:
        if int(value) > 0:
            return True
        else:
            return "Number must be > 0"
    except ValueError:
        return "Invalid input; enter a valid number"

def mark_method(lines):
    """ marks a location as visited """
    if get_any_unvisited(lines) == False:
        print("No unvisited places")
        return

    list_method(lines)
    
    print("Enter the number of a place to mark as visited")
    response = input(">>> ")
    test_number_response = test_number_mark(response, lines)
    while test_number_response != True:
        print(test_number_response)
        response = input(">>> ")
        test_number_response = test_number_mark(response, lines)
    
    location = lines[int(response)-1] # define variable location as array for the one chosen by the user
    
    if location[3] == "v":
        print("That place is already visited")
        return
    
    lines[int(response)-1][3] = "v"
    print(f"{location[0]} in {location[1]} visited!")

    lines = sort_by_visited(lines)
    return lines

def get_any_unvisited(lines):
    """ if there are no places left to visit, return false so the full function above doesn't run """
    for line in lines:
        if line[3] == "n":
            return True
    return False

def test_number_mark(value, lines):
    """ checks if number input is valid, if not requests again """
    try:
        value = int(value)
        if value > 0:
            if value > len(lines):
                return "Invalid place number"
            else:
                return True
        else:
            return "Number must be > 0"
    except ValueError:
        return "Invalid input; enter a valid number"

def quit_method(lines):
    """ runs when the program ends to save to file and quit program """
    list = open(LIST_FILE_NAME, "w")
    content = ""

    for line in lines:
        content += f"{line[0]},{line[1]},{line[2]},{line[3]}\n" # returning array to csv line string
    list.write(content)
    print(f"{len(lines)} places saved to {LIST_FILE_NAME}")
    print("Have a nice day :)")

if __name__ == '__main__':
    main()