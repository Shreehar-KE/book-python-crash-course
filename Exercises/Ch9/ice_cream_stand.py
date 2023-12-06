class Restaurant:
    """An object oriented representation of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializes restaurant's attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """prints the restaurant's description"""
        print(f'{self.restaurant_name}, A {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        """simulates opening of the restaurant"""
        print(f'The {self.restaurant_name} restaurant is now open...!')

    def set_number_served(self, value):
        """modifies the number_served value with given value"""
        if value > 0:
            self.number_served = value
        else:
            print('Error: No negative values are allowed as input..!')

    def increment_number_served(self, value):
        """increments the number_served value by given value"""
        self.number_served += value


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """initializes the attributes of Ice Cream Stand Class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """displays the availables flavors from the flavors list"""
        print('The available flavors are: ')
        for flavor in self.flavors:
            print(f'  - {flavor}')
        print()


my_ice_cream_stand = IceCreamStand("Florean Fortescue's", "Ice Cream Parlour", [
                                   'Magical Strawberry', 'Peanut Butter'])
my_ice_cream_stand.display_flavors()
