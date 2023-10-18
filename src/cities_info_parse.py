#Cities data source: https://simplemaps.com/data/pl-cities

import json
from unidecode import unidecode

path = '..\\res\\data\\cities.json'

cities_data = []

with open(path, 'r', encoding='utf-8') as file:
    cities_data = json.load(file)

#Sort by population
cities_data = sorted(cities_data, key=lambda city: int(city['population']), reverse=True)

#Keeping only the top 10
cities_data = cities_data[:10]

#Removing excess attributes
tmp = []
for city in cities_data:
    tmp.append({'name': city['city'], 'province': city['admin_name'], 'population': int(city['population'])})
cities_data = tmp

#Getting rid of non UTF-8 characters
for city in cities_data:
    city['name'] = unidecode(city['name'])
    city['province'] = unidecode(city['province'])

#Changing Warsaw to Warszawa
for city in cities_data:
    if city['name'] == 'Warsaw':
        city['name'] = 'Warszawa'

def get_10_biggest_cities():
    return cities_data