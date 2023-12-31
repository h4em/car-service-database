#Cars data source: https://github.com/arthurkao/vehicle-make-model-data/blob/master/json_data.json 
#(found on github, shoutout to https://github.com/arthurkao)

import json
import random

path = '..\\res\\data\\cars.json'

with open(path, 'r') as file:
    cars = json.load(file)

def random_car():
    '''
    Returns data about a random car.

    return: dictionary with attributes describing a car:
        - 'year' (int)
        - 'make' (str)
        - 'model' (str)
        
    rtype: dict 
    '''
    r = random.randint(0, len(cars) - 1)
    return cars[r]