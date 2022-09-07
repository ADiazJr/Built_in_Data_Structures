# Task 1a)
def pi_month():
    months_of_year = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
    print(months_of_year[2])
#1b)
def print_fruits_or_veggies():
    fruits_or_veggies = {'apple', 'banana', 'tomato', 'lettuce', 'strawberry'}
    fruits_or_veggies.add('mango')
    fruits_or_veggies.add('grape')
    fruits_or_veggies.add('eggplant')
    fruits_or_veggies.add('pepper')
    for item in fruits_or_veggies:
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