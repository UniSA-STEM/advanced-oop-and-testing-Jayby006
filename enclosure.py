'''
File: enclosure.py
Description: Store information about an enclosure and manage animals inside it.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''
from animal import Animal

class Enclosure:

    """
    The Enclosure class stores animals that belong to one category only and it also tracks cleanliness and provides a status report.
    """

    def __init__(self, name, environment_type, size, allowed_category):
        self.__name = name
        self.__environment_type = environment_type   
        self.__size = size                        
        self.__allowed_category = allowed_category   
        self.__cleanliness = "Clean"
        self.__animals = []                        

    def get_name(self):      #simple gatters.
        return self.__name

    def get_environment_type(self):
        return self.__environment_type

    def get_allowed_category(self):
        return self.__allowed_category

    def get_animals(self):
        return self.__animals
    

    #adding and removing animals
    def add_animal(self, animal):   
        if animal.get_category() != self.__allowed_category:  # check if animal belongs to the correct category
            print("Cannot add " + animal.get_name() + " to " + self.__name + " (wrong category).")
            return

        if animal.has_active_issue():  # check if animal has an active health issue
            print("Cannot add " + animal.get_name() + " to " + self.__name + " (animal is under treatment).")
            return

        if animal not in self.__animals:  # add if not already inside
            self.__animals.append(animal)
            animal.set_enclosure(self)
            print(animal.get_name() + " added to " + self.__name + ".")

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.set_enclosure(None)
            print(animal.get_name() + " removed from " + self.__name + ".")

       #cleanliness controls
    def dirty(self):
        self.__cleanliness = "Dirty"

    def clean(self):
        self.__cleanliness = "Clean"

    def get_status(self): # enclosure status report
        animal_names = ""     # build a comma separated list of names

        count = 0
        for animal in self.__animals:
            if count == 0:
                animal_names = animal.get_name()
            else:
                animal_names = animal_names + ", " + animal.get_name()
            count = count + 1

        if count == 0:    # if empty enclosure
            animal_names = "No animals"

        status = "Enclosure: " + self.__name
        status = status + " | Environment: " + self.__environment_type
        status = status + " | Cleanliness: " + self.__cleanliness
        status = status + " | Animals: " + animal_names
        return status

