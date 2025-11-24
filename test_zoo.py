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

