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

class Zookeeper(Staff):

    def feed_animal(self, animal):
        print(self.get_name() + " feeds " + animal.get_name())
        animal.eat()

    def clean_enclosure(self, enclosure):
        print(self.get_name() + " cleans " + enclosure.get_name())
        enclosure.clean()

class Veterinarian(Staff):

    def health_check(self, animal):
        print(self.get_name() + " checks " + animal.get_name())
        issues = animal.get_health_issues()

        if len(issues) == 0:
            print("No recorded health issues.")
        else:
            for issue in issues:
                print(
                    "Issue:", issue["description"],
                    "| Severity:", issue["severity"],
                    "| Active:", issue["active"])
                
    def create_treatment(self, animal, description, date_reported, severity, treatment):
        message = self.get_name() + " records health issue for " + animal.get_name()
        print(message)
        animal.add_health_issue(description, date_reported, severity, treatment)
