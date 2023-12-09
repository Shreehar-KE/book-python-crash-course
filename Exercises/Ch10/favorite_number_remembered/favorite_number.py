import json
from pathlib import Path


def get_favorite_number_from_json(path):
    """reads the number from path, if exists returns it or else returns None"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None


def get_new_favorite_number(path):
    """get new favorite number from user and stores it in path"""
    while True:
        try:
            number = int(input('Enter your favorite number: '))
        except ValueError:
            print('\nEnter numberical values only...!\n')
        else:
            contents = json.dumps(number)
            path.write_text(contents)
            return number


def favorite_number():
    """driver function for the whole program"""
    path = Path('favorite_number.json')
    number = get_favorite_number_from_json(path)

    if number:
        print(f'Your Favorite number is {number}')
    else:
        number = get_new_favorite_number(path)
        print(f'Your favorite number {number} is now stored...!')


favorite_number()
