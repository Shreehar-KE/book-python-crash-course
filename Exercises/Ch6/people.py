"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionar-
ies in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""


person_1 = {
    'first_name': 'Tony',
    'last_name': 'Stark',
    'age': '53',
    'city': 'New York'
}

person_2 = {
    'first_name': 'Steve',
    'last_name': 'Rogers',
    'age': '105',
    'city': 'New York'
}

person_3 = {
    'first_name': 'Thor',
    'last_name': 'Odinson',
    'age': '1500',
    'city': 'Asgard'
}

persons = [person_1, person_2, person_3]

for person in persons:
    print(f'{person["first_name"]} {person["last_name"]}, {person["age"]}')
    print(f'{person["city"]}\n')
