from django.shortcuts import render


def index(request):
    """The home page for Monty's Pizzeria."""
    return render(request, 'pizzas/index.html')
