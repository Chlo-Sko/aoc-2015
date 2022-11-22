# Imports
from Day import Day

# Create Day Class Object
day = Day(2, 'I Was Told There Would Be No Math')

# Create Boxes
def create_boxes():

    # Initialize Box List
    boxes = []

    # Get Input, Create Boxes
    for line in open(day.input_filename):
        l,w,h = [int(i) for i in line.split('x')]
        box = Box(l,w,h)
        boxes.append(box)

    return boxes

# Combine Wrapping Paper & Ribbon Functions to Calculate Total Supplies Needed
def order_wrapping_supplies():
    boxes = create_boxes()
    order_wrapping_paper(boxes)
    order_bow_ribbon(boxes)

# Function to Calculate Wrapping Paper Order
def order_wrapping_paper(boxes):
    # Initialize Sum
    total_dimensions = 0
    # Get Boxes, Process and Calculate Dimensions
    for box in boxes:
        total_dimensions += box.total_paper_dimensions
    print("Total Square Feet of Wrapping Paper Needed: ", total_dimensions)

# Function to Calculate Bow
def order_bow_ribbon(boxes):
    # Initialize Sum
    total_feet = 0

    # Get Boxes, Process and Calculate Dimensions
    for box in boxes:
        total_feet += box.total_ribbon_dimensions
    print("Total Feet of Ribbon Needed for Bows: ", total_feet)

# Define Box Class
class Box:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.total_paper_dimensions = self.get_box_surface_area() + self.get_slack_area()
        self.total_ribbon_dimensions = self.get_bow_perimeter() + self.get_bow_cubic_volume()

    # Takes Length, Width and Height as Input and Calculates Surface Area
    def get_box_surface_area(self):
        surface_area = (2 * self.length * self.width) + (2 * self.width * self.height) + (2 * self.height * self.length)
        return surface_area

    # Takes Length, Width and Height as Input and Calculates Area of Smallest Side
    def get_slack_area(self):
        sides = [self.length, self.width, self.height]
        sides.sort()
        smallest_side_area = sides[0] * sides[1]
        return smallest_side_area

    def get_bow_perimeter(self):
        sides = [self.length, self.width, self.height]
        sides.sort()
        smallest_sides_perimeter = (sides[0]*2) + (sides[1]*2)
        return smallest_sides_perimeter

    def get_bow_cubic_volume(self):
        return self.length * self.width * self.height