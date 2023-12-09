def city_country(city, country, population=''):
    """returns a formatted output of the city and the country"""
    if population:
        res = f'{city.title()}, {country.title()} - population {population}'
    else:
        res = f'{city.title()}, {country.title()}'
    return res
