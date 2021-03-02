"""PlaceCollection Class"""

from place import Place

class PlaceCollection:
    """ PlaceCollection object """
    def __init__(self):
        """
        Construct PlaceCollection object
        """
        self.places = []
    
    def __str__(self):
        """
        Returns JSON object as string
        :return: Message formatted for console program
        """
        response = ''
        for place in self.places:
            # Set max length variables for each value of the Place objet
            max_name_length = 0
            max_country_length = 0
            max_priority_length = 0
            if len(place.name) > max_name_length:
                max_name_length = len(place.name)
            if len(place.country) > max_country_length:
                max_country_length = len(place.country)
            if len(str(place.priority)) > max_priority_length:
                max_priority_length = len(str(place.priority))
        for i, place in enumerate(self.places):
            is_visited_star = ' ' if place.is_visited == True else '*' # Display whether or not a place has been visited
            # Add line separator for all lines but the first
            if i > 0:
                response += '\n'
            # Define strings to correctly indent values
            counter = f'{i+1:{len(str(len(self.places)+1))}}' # Finding the string length of the number used to count places
            name = f'{place.name:{max_name_length}}'
            country = f'{place.country:{max_country_length}}'
            priority = f'{place.priority:{max_priority_length}}'

            response += f"{is_visited_star}{counter}. {name} in {country} priority {priority}"
        return response
    
    def to_boolean(self, value):
        """
        Returns true if the value is string 'True' or if place is marked as visited with string 'v'
        :params value: Value to be determined whether it is a True or False parameter
        :return: Boolean depending on value argument
        """
        value = value.strip()
        if value == 'True' or value == 'v':
            return True
        else:
            return False
    
    def load_places(self, file_location):
        """
        Load places into class from provided .csv file location
        :params file_location: Specified location of csv file to use
        :return: None
        """
        file = open(file_location, 'r')
        places_raw = [place for place in file] # Create list of places from csv file
        file.close()

        for place in places_raw:
            self.add_place(place)
    
    def add_place(self, place_raw):
        """
        Add place to list
        :params place_raw: Raw string containing csv-formatted line to convert to Place object
        :return: None
        """
        place = str(place_raw).split(',')
        name = place[0]
        country = place[1]
        priority = place[2]
        is_visited = self.to_boolean(place[3])
        self.places.append(Place(name, country, priority, is_visited)) # Create Place object and add to places list

    def get_unvisited(self):
        """
        Returns count of places not yet visited
        :return: Amount of places not yet visited
        """
        unvisited_counter = 0
        for place in self.places:
            if place.is_visited == False:
                unvisited_counter += 1
        return unvisited_counter
    
    def sort(self, type):
        """
        Sort places by method provided
        :params type: Determines method to sort list by
        :return: None
        """
        # List all methods to sort by and their corresponding key function
        methods = [
            ('priority', self.sort_by_priority),
            ('name', self.sort_by_name),
            ('country', self.sort_by_country),
            ('is_visited', self.sort_by_visited)
        ]
        # Find specified method function
        for method in methods:
            if type == method[0]:
                # Sort by priority then specified key
                self.places = sorted(self.places, key=self.sort_by_priority)
                self.places = sorted(self.places, key=method[1])
    
    def sort_by_priority(self, value):
        """
        Sort by priority
        :params value: place in list to be sorted
        :return: key to sort by
        """
        return int(value.priority)
    
    def sort_by_name(self, value):
        """
        Sort by name alphabetically
        :params value: place in list to be sorted
        :return: key to sort by
        """
        return str(value.name)
    
    def sort_by_country(self, value):
        """
        Sort by country alphabetically
        :params value: place in list to be sorted
        :return: key to sort by
        """
        return str(value.country)
    
    def sort_by_visited(self, value):
        """
        Sort by visited boolean
        :params value: place in list to be sorted
        :return: key to sort by
        """
        boolean = 1 if value.is_visited else 0
        return boolean
    
    def save_places(self, file_location):
        """
        Save places to specified .csv file
        :params file_location: Location of file to save csv content to
        :return: None
        """
        file = open(file_location, 'w')
        content = ''

        # Format collection for csv file
        for place in self.places:
            is_visited = 'v' if place.is_visited else 'n'
            content += "{},{},{},{}\n".format(place.name, place.country, place.priority, is_visited)
        
        file.write(content)
        file.close()