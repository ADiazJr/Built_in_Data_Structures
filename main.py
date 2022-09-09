import implementation
from linked_list import LinkedList
from binary_node import BinaryNode

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

    binary_tree = BinaryNode(1000)
    binary_tree.insert_node(500)
    binary_tree.insert_node(1500)
    binary_tree.insert_node(250)
    binary_tree.insert_node(1250)
    binary_tree.insert_node(750)
    print(binary_tree.search_for_node(1500))
    print(binary_tree.search_for_node(750))
    print(binary_tree.search_for_node(3402))
    
    binary_tree.inorder(binary_tree)
    binary_tree.preorder(binary_tree)

main()