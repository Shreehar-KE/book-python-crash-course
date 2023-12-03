favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

persons = ['john', 'phil', 'max', 'sarah']

for person in persons:
    if person in favorite_languages.keys():
        print(f'Thank you {person.title()} for taking the poll.')
    else:
        print(f'{person.title()}, you are kindly invited to take the poll.')
