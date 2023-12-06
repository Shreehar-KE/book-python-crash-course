"""A class to represent a die"""

from random import randint


class Die:
    """Object oriented representation of a die"""

    def __init__(self, sides):
        """initializes the die's attributes like sides"""
        self.sides = sides

    def roll_die(self):
        """simulates the rolling of a die and displays the result"""
        print(randint(1, self.sides))
