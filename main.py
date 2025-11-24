'''
File: main.py
Description: Description: This is the main script that showing animals, enclosures and staff working together.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian


def main():

    print("=== Creating animals... ===")
    lion = Mammal("Leo", "Lion", 5, "Meat")
    parrot = Bird("Polly", "Parrot", 2, "Seeds")
    snake = Reptile("Snake", "Python", 3, "Rodents")
    print("Created animals:", lion.get_name(), ",", parrot.get_name(), ",", snake.get_name())
    print()

    print("=== Creating enclosures... ===")
    savannah = Enclosure("Savannah Plains", "Savannah", 500, "mammal")
    aviary = Enclosure("Tropical Aviary", "Rainforest", 200, "bird")
    reptile_house = Enclosure("Reptile House", "Desert", 150, "reptile")
    print("Created enclosures:", savannah.get_name(), ",", aviary.get_name(), ",", reptile_house.get_name())
    print()

    print("=== Creating staff...===")
    keeper = Zookeeper("Jayanga", "ZK001")
    vet = Veterinarian("Mark", "VT001")
    print("Created staff:", keeper.get_name(), "(Zookeeper),", vet.get_name(), "(Veterinarian)")
    print()



    print("=== Assigning staff to enclosures and animals...===")
    keeper.assign_enclosure(savannah)
    keeper.assign_enclosure(aviary)
    keeper.assign_enclosure(reptile_house)

    vet.assign_animal(lion)
    vet.assign_animal(snake)
    print(keeper.get_name() + " assigned to all enclosures.")
    print(vet.get_name() + " assigned to", lion.get_name(), "and", snake.get_name())
    print()

    print("=== Adding animals to enclosures... === ")
    savannah.add_animal(lion)
    aviary.add_animal(parrot)
    reptile_house.add_animal(snake)
    print()


    print("=== Zookeeper feeds animals and cleans enclosures... ===")
    keeper.feed_animal(lion)
    keeper.feed_animal(parrot)

    keeper.clean_enclosure(savannah)
    keeper.clean_enclosure(aviary)
    keeper.clean_enclosure(reptile_house)
    print()

    print("=== Veterinarian health checks...===")
    print("Initial health check for Leo:")
    vet.health_check(lion)
    print()

    print("Recording a health issue for Leo...")
    vet.create_treatment(
        lion,
        "Limping on back leg",
        "2025-11-24",
        "moderate",
        "Rest and medicine for 5 days."
    )
    print()

    print("Health check for Leo after recording issue:")
    vet.health_check(lion)
    print()

    print("=== Trying to move Leo (under treatment) to the aviary...===")
    aviary.add_animal(lion)  
    print()

    print("Final enclosure status reports:")
    print(savannah.get_status())
    print(aviary.get_status())
    print(reptile_house.get_status())


if __name__ == "__main__":
    main()
