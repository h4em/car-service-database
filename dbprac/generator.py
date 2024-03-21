import os
import random
import requests
from faker import Faker
from unidecode import unidecode
from datetime import datetime
from dotenv import load_dotenv

import utils

from db.models import *

class Generator():
    def __init__(self):
        self.fake = Faker('pl_PL')
    
    def random_email(self, f_name: str, l_name: str):
        f_name = utils.remove_whitespace(f_name).lower()
        l_name = utils.remove_whitespace(l_name).lower()

        f_name = unidecode(f_name)
        l_name = unidecode(l_name)

        separator = random.choice(['', '-', '_'])

        return f_name.lower() + separator + l_name.lower() + str(random.randint(1, 999)) + self.fake.free_email_domain()
    
    def random_person(self) -> Person:
        sex = random.choice(['F', 'M'])
    
        if sex == 'F':
            f_name = self.fake.first_name_female()
            l_name = self.fake.last_name_female()
        else:
            f_name = self.fake.first_name_male()
            l_name = self.fake.last_name_male()

        phone_num = random.choice([None, self.fake.numerify(text='### ### ###')])
        email = self.random_email(f_name, l_name)    

        return Person(f_name, l_name, sex, phone_num, email)
    
    def make_employee(self, person: Person, department: Department, position: Position) -> Employee:
        id = person.id
        date_of_birth = self.fake.date_of_birth(minimum_age=18) # type = <class 'datetime.date'>
        pesel = self.fake.pesel(date_of_birth=date_of_birth, sex=person.sex)
        position_id = position.id
        department_id = department.id

        employment_date = self.fake.date_time_between(start_date=datetime(2002, 1, 1), end_date=datetime.now()).date()
        leave_date = random.choices([None, self.fake.date_time_between(start_date=employment_date, end_date=datetime.now())], [0.82, 0.1])[0]

        if leave_date is not None:
            leave_date = leave_date.date()

        return Employee(id, pesel, position_id, department_id, employment_date, leave_date)

    def random_car(self) -> Car:
        load_dotenv()
        api_key = os.getenv('NINJAS_API_KEY')

        while True:
            year = random.randint(1980, 2024)
            url = f'https://api.api-ninjas.com/v1/cars?year={year}&limit=1'
            
            response = requests.get(url, headers={'X-Api-Key': api_key})
            data = response.json()
            
            if data:  # If data is not empty an empty list
                make = data[0]['make']
                model = data[0]['model']
                year = data[0]['year']
                break 

        license_plate = self.fake.license_plate()
        print(make, model, year, license_plate)

gen = Generator()
for _ in range(0, 5):
    gen.random_car()

# instance.__dict__ -> object's writable attributes, does not include methods or attributes inherited 
# dir(instance) -> object's attributes and methods (everything)
# inspect.getsource(obj) -> return the text of the source code for an object. inspect module 
    
# birth_date_time = self.fake.date_time_between(datetime(1945, 5, 8), datetime.now() - timedelta(days=18*365))        