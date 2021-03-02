"""Animal class."""


class Animal:
    """Animal class for storing details of a Animal."""

    def __init__(self, species="Rabbit", distance_well=10, is_thirsty=False):
        """Initialise an Animal."""
        self.species = species
        self.distance_well = distance_well
        self.is_thirsty = is_thirsty

    def __str__(self):
        """Return a string representation of an Animal."""
        return "{} {:,.2f}Km ({})".format(self.species, self.distance_well, self.is_thirsty)

    def __lt__(self, other):
        """Less than, used for sorting Animals - by distance from the well."""
        return self.distance_well < other.distance_well
