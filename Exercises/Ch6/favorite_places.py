"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person's name and their favorite places.
"""


favorite_places = {
    "Star-Lord": ["Knowhere", "Xandar", "Ego"],
    "Spider-Man": ["New York", "Venice", "Titan"],
    "Ant-Man": ["Quantum Realm", "Avengers Compound", "San Quentin"],
}

for person in favorite_places.keys():
    print(f'Favorite places of {person} are: ')
    for place in favorite_places[person]:
        print(f'    {place}')
    print()
