"""Place Class"""

IMPORTANT_PRIORITY = 2

class Place:
    """ Place object """
    def __init__(self, name=None, country=None, priority=None, is_visited=False):
        """
        Construct Place object
        :params name: Sets the name of the place being created
        :params country: Sets the country of the place being created
        :params priority: Sets the priority of the place being created
        :params is_visited: Sets the visited status of the palce being created
        """
        self.name = name
        self.country = country
        self.priority = int(priority)
        self.is_visited = is_visited
    
    def __str__(self):
        """
        Return string when called
        :return: String formatted "name,country,priority,is_visited" matching a CSV file
        """
        return f"{self.name},{self.country},{self.priority},{self.is_visited}"
    
    def visit(self, *args):
        """
        Set place to visited
        :return: None
        """
        self.is_visited = True
    
    def unvisit(self, *args):
        """
        Set place to not visited
        :param *args: Allows binding to buttons in Kivy app as it ignores the "instance" argument for console program compatibility
        :return: None
        """
        self.is_visited = False
    
    def is_important(self):
        """
        Return boolean if place is of important priority
        :return: Boolean depending on importance of visited the place
        """
        if self.priority <= IMPORTANT_PRIORITY:
            return True
        else:
            return False