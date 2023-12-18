"""Defining URL patterns for pizzas."""

from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    # A page to display the menu of pizzas available.
    path('menu', views.menu, name="menu"),
    # A page to display details of a single pizza.
    path('menu/<int:pizza_id>', views.pizza, name="pizza")
]
