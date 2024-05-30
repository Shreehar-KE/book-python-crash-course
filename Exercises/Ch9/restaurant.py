"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating 
that the restaurant is open.

     Make an instance called restaurant from your class. Print the two attributes 
individually, and then call both methods.
"""


class Restaurant:
    """An object oriented representation of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes restaurant's attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant's description"""
        print(f'{self.restaurant_name}, A {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        """simulates opening of the restaurant"""
        print(f'The {self.restaurant_name} restaurant is now open...!')


my_restaurant = Restaurant("Katz's Deli", "Kosher-Style")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())
