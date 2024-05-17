# first it starts from left last node(prints it) and then move to the right last node(prints it) and then prints the
# parent then it moves to the another side and go on.last it prints the root ,last it terminates.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # easy method
    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value)

    # second method
    def dfs_post_order(self):
        result = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
            result.append(current_node.value)

        traversal(self.root)
        return result


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.post_order(tree.root)
print('\n second method: ')
print(tree.dfs_post_order())
