def city_country(city, country, population=0):
    if population > 0: 
        result = f'{city}, {country} - population {population}'
    else: 
        result = f'{city}, {country}'
    return result.title()