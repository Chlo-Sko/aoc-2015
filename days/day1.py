# Imports
from Day import Day

# Create Day Class Object
day = Day(1, 'Not Quite Lisp')

def find_floor():
    input = day.input
    floor = 0
    for character in input:
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1

    return(floor)
