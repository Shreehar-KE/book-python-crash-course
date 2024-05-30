"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sand-
wich that's being ordered. Call the function three times, using a different num-
ber of arguments each time.
"""


def make_sandwich(*ingredients):
    """prints the message for the ordered sandwich with given ingredients"""
    print('\nMaking a sandwich with following ingredient(s):')

    for ingredient in ingredients:
        print(f'  -{ingredient}')


make_sandwich('chicken', 'oninons')
make_sandwich('fish', 'pickles', 'fries')
make_sandwich('cheese')
