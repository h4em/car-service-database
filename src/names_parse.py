#Names/Surnames data source: https://gist.github.com/kpostekk/bcc1c45b9a6af6d4f7904e71722bb588/stargazers
#(found on github, parsed by me, shoutout to: https://gist.github.com/kpostekk)

import json
import random

names_male = []
names_female = []

surnames_male = []
surnames_female = []

#Read male names
with open('..\\res\data\\names_male.json', 'r') as file:
    names_male = json.load(file)

#Read female names
with open('..\\res\\data\\names_female.json', 'r') as file:
    names_female = json.load(file)

#Read male surnames
with open('..\\res\data\surnames_male.json', 'r') as file:
    surnames_male = json.load(file)

#Read female surnames
with open('..\\res\data\surnames_female.json', 'r') as file:
    surnames_female = json.load(file)
    
def random_name(gender):
    """
    Generates a random name based on the given gender.

    type gender: int (0 for female, 1 for male)

    raises:
        TypeError: if 'gender' argument is not of type int.
        ValueError: if 'gender' argument is not 0 or 1.

    return: randomly selected name
    rtype: str
    """

    if not isinstance(gender, int):
        raise TypeError('Invalid input. Arg must be of type int.')
    elif not gender == 1 and not gender == 0:
        raise ValueError('Invalid input. Correct values are: [0, 1]')

    if gender == 0:
        r = random.randint(0, len(names_female) - 1)
        return names_female[r]
    elif gender == 1:
        r = random.randint(0, len(names_male) - 1)
        return names_male[r]
    
def random_surname(gender):
    """
    Generates a random surname based on the given gender.

    type gender: int (0 for female, 1 for male)

    raises:
        TypeError: if 'gender' argument is not of type int.
        ValueError: if 'gender' argument is not 0 or 1.

    return: randomly selected surname
    rtype: str
    """
    
    if not isinstance(gender, int):
        raise TypeError("Invalid input. Arg must be of type int.")
    elif not gender == 1 and not gender == 0:
        raise ValueError('Invalid input. Correct values are: [0, 1]')
    
    if gender == 0:
        r = random.randint(0, len(surnames_female) - 1)
        return surnames_female[r]
    elif gender == 1:
        r = random.randint(0, len(surnames_male) - 1)
        return surnames_male[r]