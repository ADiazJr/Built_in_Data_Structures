# Task 1a)
class MonthsOfYear():
    def __init__(self):
        self.months_of_year = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

def pi_month():
    months_of_year = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
    print(months_of_year[2])
#1b)
class FruitsOrVeggies():
    def __init__(self):
        self.set_of_items = {'apple', 'banana', 'tomato', 'lettuce', 'strawberry'}
    
    def add_item(self, name):
        self.set_of_items.add(name)

    def print_fruits_or_veggies(self):
        for item in self.set_of_items:
            print(item)

#1c)
def print_user_profile():
    user_profile = {
        'first_name': 'peter',
        'last_name': 'parker',
        'email_address': 'spidey@gmail.com',
        'phone_number': 2324513245
    }

    print(f"""User's first name is: {user_profile['first_name']}
    User's last name: {user_profile['last_name']}
    User's Email: {user_profile['email_address']}
    User's Phone Number: {user_profile['phone_number']}
    """)

#Task 2
def print_name_relation():
    immediate_family = [
        {
            'first_name': 'Arturo',
            'last_name': 'Diaz',
            'relation': 'father'
        },
        {
            'first_name': 'Dimari',
            'last_name': 'Diaz',
            'relation': 'sister'
        },
        {
            'first_name': 'Irene',
            'last_name': 'Rodriguez',
            'relation': 'mother'
        }
    ]

    for dictionary in immediate_family:
        print(dictionary['first_name'])
        print(dictionary['relation'])