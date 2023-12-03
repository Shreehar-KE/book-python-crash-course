favorite_numbers = {
    'luffy': [56, 1, 5],
    'zoro': [2, 11],
    'nami': [73, 3, 7],
    'usopp': [4, 1],
    'sanji': [32, 5, 2]
}

for person in favorite_numbers.keys():
    print(f'The favorite numbers of {person.title()} are ')
    for number in favorite_numbers[person]:
        print(f'    {number}')
    print()
