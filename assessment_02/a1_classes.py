"""
Name: Finley Sherwood

A1 rewrite using Place and PlaceCollection classes
"""

from place import Place
from placecollection import PlaceCollection

FILE_LOCATION = 'places.csv'

def main():
    """ Main function to run """
    print('Travel Checker 2.0 - Finley Sherwood')
    
    places = PlaceCollection()
    places.load_places(FILE_LOCATION)

    display_menu()
    method = input('>>> ').upper()
    while method != 'Q':
        if method == 'L':
            list_method(places)
        elif method == 'A':
            add_method(places)
        elif method == 'M':
            mark_method(places)
        else:
            print('Invalid menu choice')
        display_menu()
        method = input('>>> ').upper()
    quit_method(places)

def display_menu():
    """
    Displays menu options when called
    :return: None
    """
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")

def list_method(places):
    """
    Lists places in PlaceCollection
    :params places: PlaceCollection object
    :return: None
    """
    places.sort('is_visited')
    print(places)
    if places.get_unvisited() > 0:
        print(f'{len(places.places)} places. You still want to visit {places.get_unvisited()} places.')
    else:
        print('No places left to visit. Why not add a new place?')

def add_method(places):
    """
    Adds place to PlaceCollection
    :params places: PlaceCollection object
    :return: None
    """
    name = get_valid_input('Name: ')
    country = get_valid_input('Country: ')
    priority = get_valid_number('Priority: ')
    places.add_place(Place(name, country, priority, False)) # Creates place object and adds it to PlaceCollection

def get_valid_input(question):
    """
    Returns a valid response to the specified question
    :params question: Question argument to be used in input
    :return: User's valid response to the specified question
    """
    response = input(question)
    while response == "":
        print("Input can not be blank")
        response = input(question)
    return response

def get_valid_number(question):
    """
    Returns a valid value for the specified question
    :params question: Question argument to be used in input
    :return: User's valid response to the specified question
    """
    value = input(question)
    valid = False
    while valid == False:
        try:
            while int(value) <= 0: # Reject values less than 0
                print('Number must be > 0')
                value = input(question)
            valid = True
        except ValueError: # Reject invalid values
            print('Invalid input; enter a valid number')
            value = input(question)
    return value

def mark_method(places):
    """
    Marks a place a visited if required
    :params places: PlaceCollection object
    :return: None
    """
    # If there are no places to visit, don't run the rest of the function
    if places.get_unvisited() == 0:
        print('No unvisited places')
        return

    list_method(places)

    print('Enter the number of a place to mark as visited')
    value = input('>>> ')
    valid = False
    while valid == False:
        try:
            while int(value) > len(places.places) or int(value) <= 0: # Reject numbers that don't match a place from list
                print('Invalid place number')
                value = input('>>> ')
            valid = True
        except ValueError: # Reject invalid values
            print('Invalid input; enter a valid number')
            value = input('>>> ')
    
    place = places.places[int(value)-1] # Sets place variable to be Place object of selected place to mark as visited
    if place.is_visited == True:
        print('That place is already visited')
        return
    
    place.visit()
    print(f'{place.name} in {place.country} visited!')

def quit_method(places):
    """
    Quits program and saves .csv
    :params places: PlaceCollection object
    :return: None
    """
    places.save_places(FILE_LOCATION)
    print(f'{len(places.places)} places saved to {FILE_LOCATION}')
    print('Have a nice day :)')

if __name__ == '__main__':
    """ Run program """
    main()