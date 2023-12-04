def make_sandwich(*ingredients):
    """prints the message for the ordered sandwich with given ingredients"""
    print('\nMaking a sandwich with following ingredient(s):')

    for ingredient in ingredients:
        print(f'  -{ingredient}')


make_sandwich('chicken', 'oninons')
make_sandwich('fish', 'pickles', 'fries')
make_sandwich('cheese')
