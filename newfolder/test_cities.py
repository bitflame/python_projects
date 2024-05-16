import city_functions 
def test_city_country():
    assert 'Santiago, Chile'== city_functions.city_country('santiago', 'chile')
def test_city_county_population():
    assert 'Santiago, Chile - Population 5000000'== city_functions.city_country('santiago', 'chile', 5000000)