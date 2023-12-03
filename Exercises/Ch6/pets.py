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
