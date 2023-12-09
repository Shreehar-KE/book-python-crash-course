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
