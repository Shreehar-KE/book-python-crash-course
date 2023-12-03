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
