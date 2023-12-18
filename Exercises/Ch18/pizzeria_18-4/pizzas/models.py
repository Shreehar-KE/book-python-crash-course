from django.db import models

# Create your models here.


class Pizza(models.Model):
    """A model for a Pizza that can be ordered from the Pizzeria"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the name of the pizza"""
        return self.name


class Topping(models.Model):
    """A model for a Topping that can be added to a Pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the name of the topping"""
        return self.name
