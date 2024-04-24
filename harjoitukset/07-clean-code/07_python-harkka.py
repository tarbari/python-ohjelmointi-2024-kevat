###############
# HARJOITUS 1 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.


def rectangle_area(height, width):
    """
    Returns the area of an rectangle.
    """
    return height * width


###############
# HARJOITUS 2 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.

def fruit_count(fruits: dict):
    """
    Returns the total count of all fruits in a dictionary.
    """
    result = 0
    for count in fruits.values():
        result = result + count
    return result


###############
# HARJOITUS 3 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.
# Refaktoroi funktio yksinkertaisemmaksi.

def compare_num(a, b):
    """
    Check if number a is bigger than number b.
    """
    return a > b


###############
# HARJOITUS 4 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.


def print_employee_info(
    id, 
    name, 
    title,
    competences):
    """
    Prints a formatted text based on input.
    """
    template = "\nID: " + id + "\nName: " + name + "\nTitle: " + title + "\nCompetences: " + competences + "\n"
    print(template)


###############
# HARJOITUS 5 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.
# Refaktoroi if-rakenteet siten, että siellä ei tehdä ylimääräisiä if-tarkistuksia.

def menu(choice):
    """
    Control flow function for a menu in a game.
    """
    match choice:
        case 1:
            print("This will start a new game")
        case 2:
            print("This goes to settings")
        case 3:
            print("This plays the intro video")
        case 4:
            print("This plays the credits video")
        case 5:
            print("This exits the game")
        case _:
            print("Invalid input")



###############
# HARJOITUS 6 #
###############

# Nimeä funktio ja sen muuttujat luettavammiksi.

def square_positive_numbers(input_list):
    """
    For a given list of integers, return a new list where each integer is squared
    if it is positive, otherwise, the integer is removed from the list.
    """
    result = []
    if input_list is not None:
        for i in range(len(input_list)):
            if input_list[i] > 0:
                result.append(input_list[i] * input_list[i])
    return result

