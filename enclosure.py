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
