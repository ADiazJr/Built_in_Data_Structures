class Node():
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_node(self, value_to_add):
        new_node = Node(value_to_add)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def search_list(self, search_value):
        search_comparison = self.head
        while search_comparison.next is not None:
            if search_value == search_comparison.value:
                return True
            else: 
                search_comparison = search_comparison.next
        if search_value == self.tail.value:
            return True
        return False
