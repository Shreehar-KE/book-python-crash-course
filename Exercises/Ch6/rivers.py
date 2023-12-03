rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'yellow river': 'china'
}

for river, country in rivers.items():
    print(f'The {river} runs through {country}.')

print()

for river in rivers.keys():
    print(river)

print()

for country in rivers.values():
    print(country)
