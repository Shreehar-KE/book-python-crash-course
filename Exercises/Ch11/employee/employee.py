class Employee:
    """Object oriented representation of an Employee"""

    def __init__(self, first, last, salary):
        """initializes the Employee's attributes"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """increments the salary by given amount or 5000 by default"""
        self.salary += amount
