#Streets data source: http://www.warszawska.waw.pl/ulice-t_z.html

import json
import random

path = 'res\data\streets.json'
with open(path, 'r') as file:
    streets = json.load(file)

def random_street_name():    
    r = random.randint(0, len(streets) - 1)
    return streets[r]