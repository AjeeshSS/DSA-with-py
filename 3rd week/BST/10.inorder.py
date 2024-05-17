# inorder is a traversal method ,which starts from last left side of a tree then prints(if it has no children) and
# then move to the parent (prints the parent) and check the right .if the right node has no children then print it,
# else move to the left side of that right node then continues like this.it terminates when prints all the values in it.
# root prints almost the middle.

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
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)

    # second method
    def dfs_inorder(self):
        result = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)

        traversal(self.root)
        return result


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.inOrder(tree.root)
print('\n second method: ')
print(tree.dfs_inorder())
#  inorder traversal of bst gives a sorted sequence.
