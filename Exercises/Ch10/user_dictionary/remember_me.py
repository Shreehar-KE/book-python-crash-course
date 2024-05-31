"""
10-13. User Dictionary: The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.
"""


from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = int(input("What is your age? "))
    location = input("Where do you live? ")
    user_info = {}
    user_info['name'] = username
    user_info['age'] = age
    user_info['location'] = location
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user = get_stored_username(path)

    if user:
        print(f"Welcome back, {user['name']}!")
        print(
            f"You are {user['age']} years old and you live in {user['location']}")
    else:
        user = get_new_username(path)
        print(f"We'll remember you when you come back, {user['name']}!")


greet_user()
