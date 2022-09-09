class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = BinaryNode(value)
                else:
                    return self.left.insert_node(value)
            elif value > self.data:
                if self.right is None:
                    self.right = BinaryNode(value)
                else:
                    return self.right.insert_node(value)
        else:
            self.data = value

    def search_for_node(self, search_value):
        if search_value == self.data:
            return True
        else:
            if search_value < self.data:
                if self.left == None:
                    return False
                return self.left.search_for_node(search_value)
            elif search_value > self.data:
                if self.right == None:
                    return False
                return self.right.search_for_node(search_value)

    
    def inorder(self, binary_tree):
        if binary_tree is None:
            return
        self.inorder(binary_tree.left)
        print(binary_tree.data, end=" ")
        self.inorder(binary_tree.right)

    def preorder(self, binary_tree):
        if binary_tree is None:
            return
        print(binary_tree.data, end=" ")
        self.preorder(binary_tree.left)
        self.preorder(binary_tree.right)