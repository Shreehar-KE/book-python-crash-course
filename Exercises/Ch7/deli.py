"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.
"""


sandwich_orders = ['Grilled Cheese', 'Club Sandwich', 'BLT', 'Tuna Melt']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f'I made you {sandwich}')

print('\nList of sandwiches which were made:')
for sandwich in finished_sandwiches:
    print(f'    {sandwich}')
