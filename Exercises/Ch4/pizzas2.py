pizzas = ['New York Style', 'Neapolitan', 'Sicilian']
friend_pizzas = pizzas[:]

pizzas.append('Greek Pizza')
friend_pizzas.append('Detroit Pizza')

print('My Favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
