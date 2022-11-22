# Imports
import days
from days import *


# Function to Print Greeting
def print_greeting():
    # Print Greeting
    print("Welcome to Chloe's Advent of Code!")
    print("This Advent of Code event was in 2015, but I will be completing it now, in 2022.")
    print("Please, type the number for the day you'd like to view:")

    # Print List of Days Completed
    days_completed = days.__all__
    for day_num in days_completed:
        print(day_num)

# Main Function
if __name__ == "__main__":
    print_greeting()
    day1.get_first_basement_character()
    day3.get_duplicate_house_deliveries()



