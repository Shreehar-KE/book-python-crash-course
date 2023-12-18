from django.db import models

# Create your models here.


class Meal(models.Model):
    """A model for a single meal"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the name of the meal"""
        return self.name


class MealItem(models.Model):
    """A model for a individual item of the meal"""
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """returns the name of the meal item"""
        return self.name
