sandwich_orders = ['Grilled Cheese', 'Pastrami',
                   'Club Sandwich', 'Pastrami', 'BLT', 'Tuna Melt', 'Pastrami']
finished_sandwiches = []
print('The deli has ran out of pastrami..!\n')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f'I made you {sandwich}')

print('\nList of sandwiches which were made:')
for sandwich in finished_sandwiches:
    print(f'    {sandwich}')
