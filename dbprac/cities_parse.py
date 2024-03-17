#Cities data source: https://simplemaps.com/data/pl-cities

import json
from unidecode import unidecode

path = '..\\res\\data\\cities.json'

cities = []

with open(path, 'r', encoding='utf-8') as file:
    cities = json.load(file)

#Sort by population
cities = sorted(cities, key=lambda city: int(city['population']), reverse=True)

#Keeping only the top 10
cities = cities[:10]

#Removing excess attributes
tmp = []
for city in cities:
    tmp.append({'name': city['city'], 'province': city['admin_name'], 'population': int(city['population'])})
cities = tmp

#Getting rid of non UTF-8 characters
for city in cities:
    city['name'] = unidecode(city['name'])
    city['province'] = unidecode(city['province'])

#Changing Warsaw to Warszawa
for city in cities:
    if city['name'] == 'Warsaw':
        city['name'] = 'Warszawa'

def get_10_biggest_cities():
    return cities