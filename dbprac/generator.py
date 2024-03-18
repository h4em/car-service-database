import random
from faker import Faker
from unidecode import unidecode

from db.models import *

class Generator():
    def __init__(self):
        self.fake = Faker('pl_PL')

    @staticmethod
    def remove_whitespace(text: str) -> str:
        return text.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

    def random_email(self, f_name: str, l_name: str):
        f_name = self.remove_whitespace(f_name).lower()
        l_name = self.remove_whitespace(l_name).lower()

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
    
    def make_employee(self, person: Person) -> Employee:
        date_of_birth = self.fake.date_of_birth(minimum_age=18) # type = <class 'datetime.date'>
        pesel = self.fake.pesel(date_of_birth=date_of_birth, sex=person.sex)
        
        # random employment and leave date, leave date can be null, construtor takes in 'date' from datetime 
        # get_position_list, random position, a departament chyba trza bedzie zrobic assign albo tak samo ze na sztywno
        # liste departamentow

        return Employee(pesel, )

gen = Generator()
for _ in range(0, 101):
    p = gen.random_person()
    gen.make_employee(p)

# instance.__dict__ -> object's writable attributes, does not include methods or attributes inherited 
# dir(instance) -> object's attributes and methods (everything)
# inspect.getsource(obj) -> return the text of the source code for an object. inspect module 
    
# birth_date_time = self.fake.date_time_between(datetime(1945, 5, 8), datetime.now() - timedelta(days=18*365))        
    
'''
popular_car_makes = [
    "Toyota",
    "Volkswagen",
    "Ford",
    "Honda",
    "Chevrolet",
    "Mercedes-Benz",
    "BMW",
    "Tesla",
    "Audi",
    "Hyundai",
    "Nissan",
    "Kia",
    "Porsche",
    "Subaru",
    "Lexus",
    "Mazda",
    "Dodge",
    "Peugeot",
    "Jeep",
    "Renault"
]
'''