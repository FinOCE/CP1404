"""Jungle question"""
from random import randint

from animal import Animal

JUNGLE_DATA = 'jungle_data.txt'

def main():
    animals = get_animals()
    print(f'There are {len(animals)} animals in the jungle and ({len([1 for animal in animals if animal.is_thirsty])} are thirsty)')
    print(f'The maximum distance of an animal from the well is {animals[0].distance_well:.2f}Km')
    species = get_species(animals)
    species_string = str(species)[1:-1].replace("'", '') # There are many ways to do this, I did it this way because its simple, only takes one line, and automatically does the correct commas
    print(f'You have animals of {len(species)} species:\n{species_string}')
    print(f"Today's random animal is:\n{animals[randint(0, len(species))]}")

def get_animals():
    file = open(JUNGLE_DATA)
    jungle_data = [line.split(',') for line in file]
    animals = []
    for animal in jungle_data:
        species = animal[0]
        distance_well = float(animal[1].replace('*', '').strip())
        is_thirsty = True if '*' in animal[1] else False
        animals.append(Animal(species, distance_well, is_thirsty))
    return sorted(animals, reverse=True)

def get_species(animals):
    species = set()
    [species.add(animal.species) for animal in animals]
    return species

if __name__ == '__main__':
    main()