# Omar Diaa Abdelhaleem Abdullat
# Computer Science 30
# October 22, 2021 (Modified November 2)
# RPG Simple menu


# Introduction and rules.
while True:
    f = input("Lets start the game. press F to start.")
    try:
        if f == "F":
            break
        else:
            raise Exception("Goodbye.")
    except:
        print("Try Again")



def menu():
    print('''Let's get started by completing one of the following actions: 
*Explore
*Fly
*Cook
*Inventory
*Map
*Quit''')
    while True:
        choice = input("Action:")
# The First Choice starts here.
        if choice == "Explore":
            print("You explore around and you find 2 doors, door 1 and 2")
            Exploring = input("Do you go into door 1 or 2? ")
            if Exploring == "1":
                print("You go in and you find an octupus in a cage!")
            elif Exploring == "2":
                print("You go in and find a room full of guns!")
            elif Exploring == "Quit":
                print("Goodbye.")
                break
            else:
                print("Please input a valid answer.")
# The Second choice starts here.
        elif choice == ("Fly"):
            print("You go into the cockpit")
            Flying = input("Do you want to be the Pilot or Navigator? ")
            if Flying == "Pilot":
                print("You are now in full control of the space ship.")
            elif Flying == "Navigator":
                print("You are now the Navigator")
            elif Flying == "Quit":
                print("Goodbye.")
                break
            else:
                print("Please input a valid answer.")
# The last choice starts here.

                                
# Quit Function and the invalid answer function.
        elif choice == "Quit":
            print("Goodbye.")
            break
        else:
            print("Please input a valid answer.")
