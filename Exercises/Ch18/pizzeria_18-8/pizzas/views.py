from django.shortcuts import render
from .models import Pizza

# Create your views here.


def index(request):
    """The home page for pizzeria."""
    return render(request, 'pizzas/index.html')


def menu(request):
    """The page for displaying the Pizzeria's Menu"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/menu.html', context)


def pizza(request, pizza_id):
    """The Details page for each Pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
