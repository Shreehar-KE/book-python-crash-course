cities = {
    'paris': {
        'country': 'france',
        'population': '11.2M',
        'fact': 'Paris was originally a Roman City called "Lutetia"'
    },
    'venice': {
        'country': 'italy',
        'population': '258K',
        'fact': 'There are no cars in Venice'
    },
    'seoul': {
        'country': 'south korea',
        'population': '10M',
        'fact': 'It is surrounded by 44 breathtaking mountains '
    }
}

for city, info in cities.items():
    print(f'{city.title()} is a city in {info["country"].title()}')
    print(f'It has a {info["population"]} population.')
    print(f'Interesting fact about {city.title()} is that {info["fact"]}.\n')
