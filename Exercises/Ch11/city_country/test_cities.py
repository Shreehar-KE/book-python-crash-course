from city_functions import city_country


def test_city_country():
    """verifying city_country() with Santiago, Chile"""
    output = city_country('santiago', 'chile')
    assert output == 'Santiago, Chile'
