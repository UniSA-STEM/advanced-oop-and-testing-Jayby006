'''
File: enclosure.py
Description: Store information about an enclosure and manage animals inside it.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:

    def __init__(self, name, environment_type, size, allowed_category):
        self.__name = name
        self.__environment_type = environment_type   
        self.__size = size                        
        self.__allowed_category = allowed_category   
        self.__cleanliness = "Clean"
        self.__animals = []                        

    def get_name(self):
        return self.__name

    def get_environment_type(self):
        return self.__environment_type

    def get_allowed_category(self):
        return self.__allowed_category

    def get_animals(self):
        return self.__animals
    
    def add_animal(self, animal):
        if animal.get_category() != self.__allowed_category:
            print("Cannot add " + animal.get_name() + " to " + self.__name + " (wrong category).")
            return

        if animal.has_active_issue():
            print("Cannot add " + animal.get_name() + " to " + self.__name + " (animal is under treatment).")
            return

        if animal not in self.__animals:
            self.__animals.append(animal)
            animal.set_enclosure(self)
            print(animal.get_name() + " added to " + self.__name + ".")

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            animal.set_enclosure(None)
            print(animal.get_name() + " removed from " + self.__name + ".")

    def dirty(self):
        self.__cleanliness = "Dirty"

    def clean(self):
        self.__cleanliness = "Clean"

    def get_status(self):
        animal_names = ""

        count = 0
        for animal in self.__animals:
            if count == 0:
                animal_names = animal.get_name()
            else:
                animal_names = animal_names + ", " + animal.get_name()
            count = count + 1

        if count == 0:
            animal_names = "No animals"

        status = "Enclosure: " + self.__name
        status = status + " | Environment: " + self.__environment_type
        status = status + " | Cleanliness: " + self.__cleanliness
        status = status + " | Animals: " + animal_names
        return status

