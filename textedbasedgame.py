# Define the player's inventory
inventory = []

# Player Starting Room
current_room = 'foyer'

# Get Players Name
username = input("Please Type your name:\n")

# Player Instructions
def show_instructions():
    print(f"Welcome Dectetive {username}.\n")
    print("You have been tasked with investigating a haunted mansion.")
    print("Through your previous investigation, you have heard many reports about a ghost who romes the halls.")
    print("Your job is to find and collect all six items before you face the ghost.")
    print("Type 'Go (direction)' (Replace direction with one of the folowing: north, south, east, or west).")
    print("To pick up an item you find, type 'Get (item)' (replace item with the name of the item).")
    print("To exit the game, type exit.")
    print("New objective: Collect the six items and defeat the ghost.")
    print("-" * 27)

    input("Press enter to start.....")

# Start the Player instructions
show_instructions()

def show_status():
    # Display info to player
    print(f"You are in {current_room}\nInventory: {inventory}\n{'-' * 27}")

def main():
    # Map
    rooms = {
        'foyer': {'north': 'living room', 'east': 'kitchen', 'south': 'bedroom', 'west': 'study'},
        'study': {'east': 'foyer', 'items': 'flashlight'},
        'bedroom': {'north': 'foyer', 'east': 'bathroom', 'items': 'keys'},
        'bathroom': {'west': 'bedroom', 'items': 'magnifying glass'},
        'kitchen': {'west': 'foyer', 'north': 'dining room', 'items': 'evidence box'},
        'dining room': {'south': 'kitchen', 'items': 'camera'},
        'living room': {'south': 'foyer', 'east': 'secret room', 'items': 'note'},
        'secret room': {'Boss': 'Ghost'}
    }

    global inventory
    global current_room

    # List of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Display info to player
    show_status()

    # Item indecator
    if "items" in rooms[current_room].keys():
        nearby_item = rooms[current_room]["items"]
        if nearby_item not in inventory:
            if nearby_item[-1] == "s":
                print(f"You see {nearby_item}\n")
            elif nearby_item[0] in vowels:
                print(f"You see an {nearby_item}\n")
            else:
                print(f"You see a {nearby_item}\n")

    # Boss Encounter
    if "Boss" in rooms[current_room].keys():
        if len(inventory) < 6:
            print(f"You lost to the {rooms[current_room]['Boss']}.")
            exit()
        else:
            print(f"You beat the {rooms[current_room]['Boss']}.")
            exit()

    # Checks if all items have been collected
    if len(inventory) == 6:
        print()
        print("You have found all the items. Now go find and beat the ghost!\n")

    # Gets the users next move
    user_input = input("Enter your move:\n")

    # Split the moves into individual words
    next_move = user_input.split(" ")

    # First word is the action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1]

        item = " ".join(item).lower()

    if action == "Go":
         try:
             current_room = rooms[current_room][direction.lower()]
             print()
             print(f"\nYou travel {direction}.\n")
         except:
             print()
             print("\nYou can't go that way.\n")


    # Picking up items
    elif action == "Get":
         try:
             if item == rooms[current_room]["items"]:
                 if item not in inventory:
                     inventory.append(rooms[current_room]["items"])
                     print()
                     print(f"\n{item} retrieved!\n")
         except:
             pass

    # Exits the game
    elif action == "Exit":
        exit()

    # Any other commands returns invalid
    else:
        print()
        print("\nInvalid Command\n")
        main()

    main()

# Starts the main game logic
main()