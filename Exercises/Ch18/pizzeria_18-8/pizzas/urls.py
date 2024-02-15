"""Defining URL patterns for pizzas."""
from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Pizzas Menu Page
    path('pizzas/', views.pizzas, name='pizzas'),
    # Toppings Page for an individual Pizza
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
]
