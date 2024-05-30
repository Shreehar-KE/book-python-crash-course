"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:

"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values
that are returned.
"""


def city_country(city, country):
    """return a string containing the city and the country"""
    return f'{city}, {country}'


print(city_country('Paris', 'France'))
print(city_country('Oslo', 'Norway'))
print(city_country('Brussels', 'Belgium'))
