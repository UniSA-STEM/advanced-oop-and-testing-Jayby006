'''
File: test_zoo.py
Description: Includes unit tests to check animals, enclosures and staff behave correctly.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian



def test_animal_validation_age():
    lion = Mammal("Leo", "Lion", -5, "Meat")
    assert lion.get_age() == 0


def test_animal_health_issue():
    parrot = Bird("Polly", "Parrot", 2, "Seeds")
    assert parrot.has_active_issue() is False

    parrot.add_health_issue("Wing injury", "2025-11-24", "high", "Rest")
    assert parrot.has_active_issue() is True


def test_enclosure_add_correct_category():
    lion = Mammal("Leo", "Lion", 5, "Meat")
    savannah = Enclosure("Savannah Plains", "Savannah", 500, "mammal")

    savannah.add_animal(lion)
    assert lion in savannah.get_animals()


def test_enclosure_reject_wrong_category():
    parrot = Bird("Polly", "Parrot", 2, "Seeds")
    savannah = Enclosure("Savannah Plains", "Savannah", 500, "mammal")

    savannah.add_animal(parrot)   
    assert parrot not in savannah.get_animals()

def test_zookeeper_feeds_animal():
    lion = Mammal("Leo", "Lion", 5, "Meat")
    keeper = Zookeeper("Anna", "ZK001")

    keeper.feed_animal(lion)   
    assert lion.get_name() == "Leo"


def test_vet_adds_treatment():
    snake = Reptile("Snek", "Python", 3, "Rodents")
    vet = Veterinarian("Mark", "VT001")

    vet.create_treatment(
        snake,
        "Skin infection",
        "2025-11-24",
        "medium",
        "Apply ointment"
    )

    issues = snake.get_health_issues()
    assert len(issues) == 1
    assert issues[0]["description"] == "Skin infection"
    assert issues[0]["active"] is True

