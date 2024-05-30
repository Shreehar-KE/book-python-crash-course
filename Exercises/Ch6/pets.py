"""
6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner's name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.
"""

pet_1 = {
    "kind": "Dog",
    "name": "Daisy",
    "owner": "John Wick"
}

pet_2 = {
    "kind": "Cat",
    "name": "Crookshanks",
    "owner": "Hermione Granger"
}

pet_3 = {
    "kind": "Platypus",
    "name": "Perry",
    "owner": "Phineas & Ferb"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f'{pet["name"]} is a {pet["kind"]} owned by {pet["owner"]}.')
