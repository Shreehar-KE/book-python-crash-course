from city_functions import city_country


def test_city_country():
    """verifying city_country() with Santiago, Chile"""
    output = city_country('santiago', 'chile')
    assert output == 'Santiago, Chile'


def test_city_country_population():
    """verifying city_country() with Santiago, Chile - population 5000000"""
    output = city_country('santiago', 'chile', population=5000000)
    assert output == 'Santiago, Chile - population 5000000'
