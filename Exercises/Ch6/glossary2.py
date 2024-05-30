"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary's keys and values. When
you're sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""


glossary = {
    'Variables': 'labels',
    'String': 'series of characters',
    'Integers': 'numerical values without fractional part',
    'Float': 'numerical values with fractional part',
    'Boolean': 'either True or False',
    'List': 'mutable dynamic sequence',
    'Tuple': 'immutable static sequence',
    'Dictionary': 'key-value pair sequence',
    'Set': 'unique sequence of values'
}

for key, value in glossary.items():
    print(f'{key}: {value}\n')
