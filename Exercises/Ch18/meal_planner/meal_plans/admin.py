from django.contrib import admin

# Register your models here.
from .models import Meal, MealItem

admin.site.register(Meal)
admin.site.register(MealItem)
