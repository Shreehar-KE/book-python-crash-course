"""
10-14. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who last
used the program.
       Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it's not, call get_new_username() to get the correct
username.
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
        verification = input(f"{user['name']} - Is this your username(y/n)? ")
        if verification.lower() == 'y':
            print(f"Welcome back, {user['name']}!")
            print(
                f"You are {user['age']} years old and you lives in {user['location']}")
        else:
            user = get_new_username(path)
            print(f"We'll remember you when you come back, {user['name']}!")
    else:
        user = get_new_username(path)
        print(f"We'll remember you when you come back, {user['name']}!")


greet_user()
