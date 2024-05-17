# preorder is a traversal method, first prints the root of a tree,then move to left(and prints) until the left ends ,
# then move to the recent parent's right and prints that and move on like that.terminates while print all values.
#

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
    def pre_order(self, root):
        if root:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)

    # second method
    def dfs_pre_order(self):
        result = []

        def traversal(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)

        traversal(self.root)
        return result


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.pre_order(tree.root)
print('\n second method: ')
print(tree.dfs_pre_order())
