sandwich_orders = ['Grilled Cheese', 'Club Sandwich', 'BLT', 'Tuna Melt']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f'I made you {sandwich}')

print('\nList of sandwiches which were made:')
for sandwich in finished_sandwiches:
    print(f'    {sandwich}')
