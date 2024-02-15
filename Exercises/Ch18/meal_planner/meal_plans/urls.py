"""Defining URL patterns for the meal_plans."""

from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Home page
    path('', views.index, name='index',)
]
