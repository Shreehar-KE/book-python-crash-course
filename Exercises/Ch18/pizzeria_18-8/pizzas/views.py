from django.shortcuts import render
from .models import Pizza


def index(request):
    """The home page for Monty's Pizzeria."""
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """List all the pizzas available in the pizzeria"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    """List all toppings of an individual pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)
