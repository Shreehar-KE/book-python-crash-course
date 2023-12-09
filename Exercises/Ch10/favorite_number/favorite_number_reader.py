import json
from pathlib import Path

path = Path('favorite_number.json')

try:
    contents = path.read_text()
except FileNotFoundError:
    print('favorite_number.json is not found...!')
else:
    number = json.loads(contents)
    print(f'Your favorite number is {number}.')
