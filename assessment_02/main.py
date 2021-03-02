"""
Name: Finley Sherwood
Date: 20/10/2020
Brief Project Description: Travel checker program using Kivy GUI
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-FinOCE
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window

from placecollection import PlaceCollection

FILE_LOCATION = 'places.csv'
GREEN = [0, 1, 0, 1]
RED = [1, 0, 0, 1]

class TravelTrackerApp(App):
    """ Main program - Kivy app to document places to visit and past trip locations """
    # Define sorting methods and default value for Kivy spinner
    sort_methods = ['name', 'country', 'priority', 'visited']
    first_sort_method = sort_methods[3]

    def __init__(self, **kwargs):
        """
        Construct main app
        :params **kwargs: Used to give TravelCheckerApp all the same initialising arguments as the Kivy App
        """
        super().__init__(**kwargs)
    
    def build(self):
        """
        Build Kivy App
        :return: Reference to root Kivy widget
        """
        self.title = "TravelChecker"
        self.root = Builder.load_file('app.kv')
        Window.bind(on_request_close=self.save_to_csv)

        # Loading, sorting, and displaying places contained in .csv file
        self.PC = PlaceCollection()
        self.PC.load_places(FILE_LOCATION)
        self.set_sort_method('visited')
        self.update_widgets()

        return self.root
    
    def set_sort_method(self, method):
        """
        Sets method for sorting and updates widgets accordingly
        :param method: String that specifies sorting method
        :return: None
        """
        method = 'is_visited' if method == 'visited' else method # Day "visited" instead of property name "is_visited" where applicable
        # Store method and update widgets to match new method
        self.current_sort_method = method
        self.update_widgets()
    
    def update_widgets(self, *args):
        """
        Updates widgets to reflect recent changes
        :param *args: Allows binding to buttons as it ignores the "instance" argument
        :return: None
        """
        self.root.ids.places_container.clear_widgets()
        self.PC.sort(self.current_sort_method)
        # Create widget for every place in collection
        for place in self.PC.places:
            self.create_widget(place)
        self.root.ids.to_visit_counter.text = f'Places to visit: {self.PC.get_unvisited()}'
    
    def create_widget(self, place):
        """
        Creates widget in place_container of app
        :param place: Place class object to create a widget of
        :return: None
        """
        button_text = f'{place.name} in {place.country}, priority {place.priority}'
        # Create temporary button object to add to container
        temp_button = Button(text=button_text, id=place.name)
        if place.is_visited:
            temp_button.text = temp_button.text + ' (visited)'
            temp_button.background_color = GREEN
        else:
            temp_button.background_color = RED
        # Set visit property of press and update widgets on release
        temp_button.bind(on_press=self.update_visit)
        temp_button.bind(on_release=self.update_widgets)
        self.root.ids.places_container.add_widget(temp_button)
    
    def add_place_to_collection(self):
        """
        Adds new place to PlaceCollection if valid, then updates widgets
        :return: None
        """
        try:
            name = str(self.root.ids.name_field.text).title()
            country = str(self.root.ids.country_field.text).title()
            if name == '' or country == '': # Handle invalid value for name and country
                self.root.ids.status.text = 'All fields must be completed'
                return

            priority = int(self.root.ids.priority_field.text)
            if priority < 0:
                self.root.ids.status.text = 'Priority must be > 0'
                return
            
            is_visited = False
            
            # Create csv-style string to parse into PlaceCollection function so GUI and console programs both work with the same class
            places_raw = str([name, country, priority, is_visited])
            places_raw = places_raw[1:len(places_raw)-1].replace(', ', ',').replace('\'', '')

            self.PC.add_place(places_raw)
            self.update_widgets()
        except ValueError: # Handle invalid value for priority
            self.root.ids.status.text = 'Please enter a valid number'
    
    def clear_fields(self):
        """
        Clears selected text fields from app
        :return: None
        """
        self.root.ids.name_field.text = ''
        self.root.ids.country_field.text = ''
        self.root.ids.priority_field.text = ''
        self.root.ids.status.text = ''
    
    def update_visit(self, instance):
        """
        Visits location in collection and updates status message
        :param instance: Instance of Kivy button that ran the function
        :return: None
        """
        # Find place object from collection that matches the button
        for place in self.PC.places:
            if place.name == instance.id:
                if place.is_visited == False:
                    """ Marking as visited """
                    place.visit()
                    message = f'You visited {place.name}.'
                    if place.is_important():
                        message += ' Great travelling!'
                else:
                    """ Marking as not visited """
                    place.unvisit()
                    message = f'You need to visit {place.name}.'
                    if place.is_important():
                        message += ' Get going!'
                self.root.ids.status.text = message
    
    def save_to_csv(self, instance):
        """
        Saves collection to specified CSV, using App function rather than directly using PlaceCollection for console program compatibility
        :param insatnce: Instance of Kivy application
        :return: None
        """
        self.PC.save_places(FILE_LOCATION)

if __name__ == '__main__':
    TravelTrackerApp().run()