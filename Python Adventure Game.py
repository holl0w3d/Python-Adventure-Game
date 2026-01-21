def start_game():
    inventory = []
    current_room = "entrance"
    play_game(current_room, inventory)


def play_game(room, items):
    while True:
        if room == "entrance":
            room = entrance_room(items)

        elif room == "hallway":
            room = hallway_room(items)

        elif room == "library":
            room = library_room(items)

        elif room == "kitchen":
            room = kitchen_room(items)

        else:
            print("Thanks for playing!")
            break


def entrance_room(items):
    print("\nYou are standing at the entrance of an old mansion.")
    choice = input("Do you want to enter or leave? ").lower()

    if choice == "enter":
        print("You walk into the dark hallway...")
        return "hallway"
    else:
        print("You decide to stay outside. Game over.")
        return None


def hallway_room(items):
    print("\nYou are in a hallway with doors to the left and right.")
    choice = input("Do you go left or right? ").lower()

    if choice == "left":
        return "library"
    elif choice == "right":
        return "kitchen"
    else:
        print("You stand still, unsure what to do.")
        return "hallway"


def library_room(items):
    print("\nYou enter a dusty library filled with old books.")

    if "key" not in items:
        choice = input("You see a shiny key. Pick it up? (yes/no): ").lower()

        if choice == "yes":
            items.append("key")
            print("You picked up the key!")

    return "hallway"


def kitchen_room(items):
    print("\nYou're in the kitchen. There's a locked door to the cellar.")

    if "key" in items:
        print("You use the key to unlock the door. You win!")
        return None
    else:
        print("The door is locked. Maybe there’s a key somewhere...")
        return "hallway"


start_game()
