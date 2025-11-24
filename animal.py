'''
File: animal.py
Description: Includes animal classes and their basic actions and health infomation
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
     def __init__(self, name, species, age, diet, category):
        if age < 0:
            age = 0    # simple data validation beacuse age cannot be negative.
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__category = category          
        self.__enclosure = None         # set later when added to an enclosure  
        self.__health_issues = []     # list of health issue dictionaries  

    #basic gatters
     def get_name(self):
        return self.__name
     
     def get_species(self):
        return self.__species

     def get_age(self):
        return self.__age

     def get_diet(self):
        return self.__diet

     def get_category(self):
        return self.__category

     def get_enclosure(self):
        return self.__enclosure

     def get_health_issues(self):
        return self.__health_issues
     
     def set_enclosure(self, enclosure):   #setter for enclosure assignment
        self.__enclosure = enclosure

      #basic animal behaviours
     def make_sound(self):
        print(self.__name + " makes a sound.")

     def eat(self):
        print(self.__name + " is eating " + self.__diet)

     def sleep(self):
        print(self.__name + " is sleeping.")

           #health management
            # add a new health issue record for this animal
     def add_health_issue(self, description, date_reported, severity, treatment):
        issue = {
            "description": description,
            "date": date_reported,
            "severity": severity,
            "treatment": treatment,
            "active": True  # active meaning the issue is still ongoing
            }
        self.__health_issues.append(issue)

     def has_active_issue(self):    # checking if any health issue is still active
        for issue in self.__health_issues:
            if issue["active"]:
                return True
        return False
     
     def __str__(self):     # text representation of the animal
        return self.__name + " the " + self.__species + " (" + self.__category + ")"

     
class Mammal(Animal):   # Mammal is subclass of Animal with a fixed category "mammal".
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet, "mammal")  # calling the parent constructor with category set to mammal.

    def make_sound(self):
        print(self.get_name() + " growls.")


class Bird(Animal):  # Bird subclass, Animal with a fixed category bird.
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet, "bird")

    def make_sound(self):   # make_sound for mammals
        print(self.get_name() + " chirps.")


class Reptile(Animal):  # Reptile subclass, Animal with a fixed category reptile
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet, "reptile")

    def make_sound(self):
        print(self.get_name() + " hisses.")


    
