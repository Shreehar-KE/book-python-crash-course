from django.db import models


class Pizza(models.Model):
    """A Class representation of a pizza"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """returns the string representation of the pizza model"""
        return self.name


class Topping(models.Model):
    """A Class representation of a topping"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        """returns the string representation of the topping model"""
        return self.name
