import random
import string
import time
from datetime import datetime, timedelta
from pesel import Pesel

import streets_info_parse
import cities_info_parse
import cars_info_parse
import names_parse

def gen_address():
    '''
    Returns a random address, (street name and number).

    return: generated adress.
    rtype: str
    '''
    street_name = streets_info_parse.random_street_name()
    street_num = str(random.randint(1, 100))

    return street_name + street_num    

def gen_email(name, surname):
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
    
    return name.lower() + random_separator() + surname.lower() + str(random_int) + '@email.com'

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

def random_char_uppercase():
    return random.choice(string.ascii_uppercase)

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

    return result.strftime('%Y-%m-%d')

def gen_later_date(date):
    '''
    Returns a random date between param date and now, 'YYYY-MM-DD' format, hyphen separated.

    return: generated date
    rtype: str
    '''
    try:
        datetime_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise TypeError("Invalid input. Arg must be in of str type.")

    current_date = datetime.now()
    
    time_between = current_date - datetime_date
    random_num_of_days = random.randint(0, time_between.days)

    result = datetime_date + timedelta(days=random_num_of_days)

    return result.strftime('%Y-%m-%d')

def gen_license_plate():
    '''
    Returns a random license plate in str format. 2 letters, space, then 5 letters/digits.

    return: generated license plate
    rtype: str
    '''
    
    result = ''
    for i in range(0, 2):
        result += random_char_uppercase()
    
    result += ' '

    for i in range(0, 5):
        r = random.randint(0, 100)
        if r % 2 == 0:
            result += random_char_uppercase()
        else:
            result += str(random.randint(0, 9))

    return result

def gen_person():
    '''
    Generates a random person's data.
    
    return: dictionary with attributes describing a person:
        - 'name' (str)
        - 'surname' (str)
        - 'gender' (int)
        - 'birth_date' (str)
        - 'social_security_num' (str)
        - 'email' (str)
        - 'phone_num' (str)
    
    rtype: dict
    '''

    gender = random_boolean()
    name = names_parse.get_random_name(gender)
    surname = names_parse.get_random_surname(gender)
    email = gen_email(name, surname)
    phone_num = gen_phone_num()

    birthdate = gen_birth_date()
    year, month, day = birthdate.split('-')

    social_security_num = str(Pesel.generate(gender, int(year), int(month), int(day)))

    result = {
        'name': name, 
        'surname': surname, 
        'gender': gender, 
        'birth_date': birthdate,
        'social_security_num': social_security_num,
        'email': email, 
        'phone_num': phone_num,
    }

    return result

for i in range(0, 20):
    person = gen_person()
    print(person)

    time.sleep(2)

input()