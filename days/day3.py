from Day import Day

# Create Day Object & Get Input
day = Day(3, 'Perfectly Spherical Houses in a Vacuum')
input = day.input

# Increment Duplicate Houses
def increment_house(x, y, houses):
    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

# Move Santa Based on Direction Provided
def calc_move(x, y, direction):
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '>':
        x += 1
    else:
        x -= 1
    return x, y

# Calculate Duplicate Houses Based on Directional Input
def get_duplicate_house_deliveries():
    santaX = 0
    santaY = 0
    robosantaX = 0
    robosantaY = 0
    houses_visited = {}
    increment_house(santaX, santaY, houses_visited)
    increment_house(robosantaX, robosantaY, houses_visited)
    santasTurn = True

    for direction in input:
        if santasTurn:
            santaX, santaY = calc_move(santaX, santaY, direction)
            increment_house(santaX, santaY, houses_visited)
            santasTurn = False
        else:
            robosantaX, robosantaY = calc_move(robosantaX, robosantaY, direction)
            increment_house(robosantaX, robosantaY, houses_visited)
            santasTurn = True
    print("Duplicate House Deliveries: ", len(houses_visited))