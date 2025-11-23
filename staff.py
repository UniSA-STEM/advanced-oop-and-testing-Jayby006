'''
File: staff.py
Description: Include staff classes and basic tasks staff perform in the zoo.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure


class Staff:
    def __init__(self, name, staff_id):
        self.__name = name
        self.__staff_id = staff_id
        self.__assigned_enclosures = []
        self.__assigned_animals = []

    def get_name(self):
        return self.__name

    def get_staff_id(self):
        return self.__staff_id

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    def get_assigned_animals(self):
        return self.__assigned_animals

    def assign_enclosure(self, enclosure):
        if enclosure not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure)

    def assign_animal(self, animal):
        if animal not in self.__assigned_animals:
            self.__assigned_animals.append(animal)