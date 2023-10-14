import random
import cities_info_parse
import streets_info_parse
import cars_info_parse
from datetime import datetime, timedelta

def get_random_city():
    '''
    Returns a dictionary describing a random city. Keys are: name, province and population.

    return: data about a random city.
    rtype: dict
    '''
    
    cities = cities_info_parse.get_10_biggest_cities()
    r = random.randint(0, len(cities) - 1)
    return cities[r]

def gen_address():
    '''
    Returns a random address, (street name and number).

    return: generated adress.
    rtype: str
    '''
    street_name = streets_info_parse.random_street_name()
    street_num = str(random.randint(1, 100))

    return street_name + street_num    

def generate_email(name, surname):
    '''
    Returns email address based on persons name and surname.

    param name: person's name
    type name: str

    param surname: person's surname
    type name: str
    
    return: generated email address
    rtype: str
    '''
    if not isinstance(name, str) or not isinstance(surname, str):
        raise TypeError("Invalid input. Both parameters must be of type str.")

    random_int = random.randint(0, 999)
    
    return name + random_separator() + surname + str(random_int) + '@email.com'

def gen_birth_date():
    '''
    Returns a random birth date from range [now - 120 years ago, now - 18 years ago],
    in 'YYYY-MM-DD' format, hyphen separated.

    return: generated birth date
    rtype: str
    '''
    current_date = datetime.now()
    
    start_date = current_date - timedelta(days=365 * 120) 
    end_date = current_date - timedelta(days=365 * 18)

    time_between = end_date - start_date

    random_num_of_days = random.randint(0, time_between.days)

    result = start_date + timedelta(days=random_num_of_days)

    return result.strftime("%Y-%m-%d")

def random_boolean():
    return random.choice([0, 1])

def random_separator():
    separators = ['', '-', '_']
    random_int = random.randint(0, len(separators) - 1)
    return separators[random_int]

def gen_phone_num():
    result = ''
    for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            result += ' '
        result += str(random.randint(0, 9))
    return result

def gen_event_date():
    '''
    Returns a random date from range [date of company establishment, now]. An event could be 
    anything that happens inside the company e.g. a dismissal, completing an order etc. 
    'YYYY-MM-DD' format, hyphen separated.

    return: random event date
    rtype: str
    '''
    establishment_date = datetime(year=2002, month=1, day=28)
    current_date = datetime.now()

    time_between = current_date - establishment_date

    random_num_of_days = random.randint(0, time_between.days)

    result = establishment_date + timedelta(days=random_num_of_days)

    return result.strftime("%Y-%m-%d")

def gen_person():
    '''
    id integer
    name varchar 20
    surname 20
    gender int
    phonenum varchar 9 N
    email varchar 20 N

    niech zwraca dict ze wszystkim
    '''

print(generate_email("hubert", "m"))
print(gen_phone_num())
print(gen_birth_date())
print(get_random_city())
print(gen_event_date())

print(cars_info_parse.random_car())

input()

#parser imion
#pesel -> z gita skrypt pesel pobrany