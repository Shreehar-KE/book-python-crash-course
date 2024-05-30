"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""


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
