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


restaurant_1 = Restaurant("Katz's Deli", "Kosher-Style")
restaurant_2 = Restaurant('Le Polidor', 'Bistro')
restaurant_3 = Restaurant('Los Pollos Hermanos', 'Fast-Food')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
