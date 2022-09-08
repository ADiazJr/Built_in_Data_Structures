from dataclasses import field
import implementation
from linked_list import LinkedList

# implementation.pi_month()
# list_object = implementation.FruitsOrVeggies()
# list_object.add_item('grape')
# list_object.add_item('pepper')
# list_object.add_item('eggplant')
# list_object.add_item('guava')
# list_object.print_fruits_or_veggies()
# implementation.print_user_profile()
# implementation.print_name_relation()

def main():
    first_list = LinkedList()
    first_list.append_node(78)
    first_list.append_node(38)
    first_list.append_node(341)
    print(first_list)
    print(first_list.search_list(341))
    print(first_list.search_list(3441))

main()