# Omar Diaa Abdelhaleem Abdullat
# Computer Science 30
# Novmeber 3, 2021
# RPG Modules and Maps


print("Here is your map: ")
# This is the array.
Map = ["Cockpit", "Kitchen", "Medbay", "Engine room", "Defence room"]

map_location = {
    "cockpit": {
        "description": "Where you control the ship"
    },
    "kitchen": {
        "description": "where you cook for the crew"
    },
    "medbay": {
        "description": "where you make chemicals"
    },
    "engine room": {
        "description": "where you service the ship"
    },
    "defence room": {
        "description": "where you get guns"
    },
    "medbay": {
        "description": "where you make chemicals"
    },
    "engine room": {
        "description": "where you service the ship"
    },
    "defence room": {
        "description": "where you get guns"
    }
}



for locations in map_location:
    for description in map_location[locations]:
        text = map_location[locations][description]
        print(f"{locations} - {text}")
      
