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
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__category = category          
        self.__enclosure = None           
        self.__health_issues = []       


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
     
     def set_enclosure(self, enclosure):
        self.__enclosure = enclosure


     def make_sound(self):
        print(self.__name + " makes a sound.")

     def eat(self):
        print(self.__name + " is eating " + self.__diet)

     def sleep(self):
        print(self.__name + " is sleeping.")


     def add_health_issue(self, description, date_reported, severity, treatment):
        issue = {
            "description": description,
            "date": date_reported,
            "severity": severity,
            "treatment": treatment,
            "active": True
            }
        self.__health_issues.append(issue)

     def has_active_issue(self):
        for issue in self.__health_issues:
            if issue["Active"]:
                return True
        return False


