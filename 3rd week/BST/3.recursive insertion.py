class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryST:
    def __init__(self):
        self.root = None

    # in normal case we don't need to pass a node to a function, but in this case we are
    #  passing a node, so we use '__'
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)


tree = BinaryST()
tree.r_insert(2)
tree.r_insert(1)
tree.r_insert(3)

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
