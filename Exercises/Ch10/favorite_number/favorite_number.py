"""
10-11. Favorite Number: Write a program that prompts for the user's favorite
number. Use json.dumps() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message “I know your favorite
number! It's _____.”
"""


import json
from pathlib import Path

path = Path('favorite_number.json')
while True:
    try:
        number = int(input('Enter your favorite number: '))
    except ValueError:
        print('\nEnter numerical values only...!\n')
    else:
        contents = json.dumps(number)
        path.write_text(contents)
        break
