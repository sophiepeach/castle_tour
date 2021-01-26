def castle_game():
    place = "entrance"
    while "quit" != place:
        if "entrance" == place:
            place = do_entrance()
        elif "dungeon" == place:
            place = do_dungeon()
        elif "tallest tower" == place:
            place = do_tower()
        elif "lake" == place:
            place = do_lake()
        elif "garden" == place:
            place = do_garden()
        else:
            print("You must be confused. Let's start over in the foyer")
            do_entrance()

    print("Thank you for visiting! Good bye")


def do_entrance():
    print("Welcome to our luxurious castle. You are in the entrance, which is called a foyer.")
    print("You are in the foyer. Type the place you would like to visit.")
    print("You can tour the: dungeon, the tallest tower, the lake, or the garden. ")
    action = input("If you would like to end your tour, you can type quit at any time. ")
    print(">>", action)
    if "dungeon" == action:
        return "dungeon"
    if "tallest tower" == action:
        return "tallest tower"
    if "lake" == action:
        return "lake"
    if "garden" == action:
        return "garden"
    elif "quit" == action:
        return "quit"
    else:
        print("You must be confused. We'll take you back to the castle entrance")
        return "entrance"


def do_dungeon():
    print("This is the dungeon. It is were prisoners were once held captive.")
    action = input("Please type entrance to return to the foyer. ")
    print(">>", action)
    if "entrance" == action:
        return "entrance"
    elif "quit" == action:
        return "quit"
    else:
        print("You must be confused. We'll take you back to the castle entrance anyway")
        return "entrance"


def do_tower():
    print("This is the tallest tower in the castle. If provides a lovely view!")
    action = input("Please type entrance to return to the foyer. ")
    print(">>", action)
    if "entrance" == action:
        return "entrance"
    elif "quit" == action:
        return "quit"
    else:
        print("You must be confused. We'll take you back to the castle entrance anyway")
        return "entrance"


def do_lake():
    print("This is the lake. The water is very dark but sometimes creature come to the surface.")
    action = input("Type entrance to go back to the castle foyer. ")
    print(">>", action)
    if "entrance" == action:
        return "entrance"
    elif "quit" == action:
        return "quit"
    else:
        print("You must be confused. We'll take you back to the castle entrance")
        return "entrance"


def do_garden():
    print("This is the garden. There are many different types of plants and some rare, exotic flowers.")
    action = input("Type entrance to go back to the castle foyer. ")
    print(">>", action)
    if "entrance" == action:
        return "entrance"
    elif "quit" == action:
        return "quit"
    else:
        print("You must be confused. We'll take you back to the castle entrance")
        return "entrance"


castle_game()
