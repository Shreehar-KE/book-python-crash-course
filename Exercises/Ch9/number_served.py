"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

     Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
     
     Add a method called increment_number_served() that lets you increment
the number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
"""


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


my_restaurant = Restaurant('Los Pollos Hermanos', 'Fast-Food')
print(f'\nNumber of customers served: {my_restaurant.number_served}')

print('\nServing to 2 Customers.')
my_restaurant.number_served = 2
print(f'\nNumber of customers served: {my_restaurant.number_served}')


print('\nServing to 2 Customers.')
my_restaurant.set_number_served(4)
print(f'\nNumber of customers served: {my_restaurant.number_served}')

print('\nServing to 3 Customers.')
my_restaurant.increment_number_served(3)
print(f'\nNumber of customers served: {my_restaurant.number_served}')
