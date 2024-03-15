import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pl_PL')
for i in dir(fake):
    print(i)

import inspect
print(inspect.getsource(fake.email))

for _ in range(0, 10):
    sex = random.choice(['F', 'M'])

    if sex == 'F':
        f_name = fake.first_name_female()
        l_name = fake.last_name_female()
    else:
        f_name = fake.first_name_male()
        l_name = fake.last_name_male()

    birth_date_time = fake.date_time_between(datetime(1945, 5, 8), datetime.now() - timedelta(days=18*365))
    birth_date_str = birth_date_time.strftime('%Y-%m-%d')
    pesel = fake.pesel(birth_date_time, sex)
    
    print(f_name, l_name, sex, birth_date_str, pesel)

    
# instance.__dict__ -> object's writable attributes, does not include methods or attributes inherited 
# dir(instance) -> object's attributes and methods (everything)
# inspect.getsource(obj) -> return the text of the source code for an object. inspect module 