# Imports
from Day import Day

# Create Day Class Object
day = Day(1, 'Not Quite Lisp')

# Calculate the Final Floor of Santa After Directions Are Provided as Input
def find_floor():
    input = day.input
    floor = 0
    for character in input:
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1

    return(floor)

# Calculate the First Character That Leads Santa into the Basement
def get_first_basement_character():
    input = day.input
    char_count = 0
    floor = 0

    for character in input:
        if character == '(':
            floor += 1
            char_count += 1
        elif character == ')':
            floor -= 1
            char_count += 1
        if floor < 0:
            print(char_count)

    print(char_count)
