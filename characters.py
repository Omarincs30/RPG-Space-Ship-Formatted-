
# Omar Diaa Abdelhaleem Abdullat
# Computer Science 30
# Novemeber 2, 2021
# RPG Inventory

characters_Dictionary = {
    " Astronaut": {
        "  floating speed": 80,
        "  description": "can go anywhere on map"
    },
    " Scientist": {
        "  floating speed": 88,
        "  description": "Can go in medbay and make chemicals"
    },
    " Mechanic": {
        "  floating speed": 60,
        "  description": "can go into engine room and do maintenance"
    },
    " Defence Operator": {
        " floating speed": 93,
        " description": "can use the defence room and kill aliens"
    },
    " Pilot": {
        " floating speed": 40,
        " description": "can fly and control the ship"
    }
}

print("Characters")
for Character in characters_Dictionary:
    print(f"{Character}: ")
    for item in characters_Dictionary[Character]:
        print(f"{item} - {characters_Dictionary[Character][item]}")

print()
p1 = input("Your Character: ")


Inventory= {
    "Map": {
        "Description": "A map of the whole ship"
    },
    "Raygun": {
        "Description": "Can be used to shoot evil aliens"
    }
}

