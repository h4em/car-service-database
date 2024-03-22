import random

from db.models import *

def remove_whitespace(text: str) -> str:
    return text.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

def random_department(departments: list) -> Department:
    department_objects = [dept['department'] for dept in departments]
    weights = [dept['weight'] for dept in departments]
        
    return random.choices(department_objects, weights=weights, k=1)[0]

def random_position(positions: list) -> Position:
    position_objects = [pos['position'] for pos in positions if pos['position'].title not in ['CEO', 'Custodian']]
    weights = [pos['weight'] for pos in positions if pos['position'].title not in ['CEO', 'Custodian']]
        
    return random.choices(position_objects, weights, k=1)[0]

# def get_random_service_id():
#     return random.randint(1, 20)

# def get_num_of_services():
#     possible = [1, 2, 3, 4]
#     weights = [0.71, 0.43, 0.19, 0.05]
#     return random.choices(possible, weights)[0]

# def get_num_of_employees():
#     possible = [1, 2, 3, 4]
#     weights = [0.65, 0.29, 0.11, 0.08]
#     return random.choices(possible, weights)[0]

# service_positions_dict = {
#     1: [2, 3, 4, 6, 9],
#     2: [2, 3, 4, 6, 9],
#     3: [2, 3, 4, 5, 6, 9],
#     4: [2, 3, 4, 5, 6, 9],
#     5: [2, 3, 4, 6, 9],
#     6: [2, 3, 4, 5, 6, 9],
#     7: [2, 3, 4, 5, 6, 11],
#     8: [2, 3, 5, 15],
#     9: [2, 3, 4, 5, 6],
#     10: [2, 3, 4, 5, 6],
#     11: [2, 3, 4, 5, 6],
#     12: [2, 3, 4, 5, 6, 15],
#     13: [2, 3, 4, 5, 6, 11, 15],
#     14: [2, 3, 4],
#     15: [2, 3, 4, 6, 7, 9],
#     16: [2, 3, 5, 15],
#     17: [2, 3, 5, 10],
#     18: [2, 3, 5, 10],
#     19: [2, 3, 5, 10],
#     20: [14]
# }