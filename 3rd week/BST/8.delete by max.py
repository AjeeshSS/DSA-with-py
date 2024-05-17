# delete a parent node by replacing a node with a max value present in left side of a tree.

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

    # traversal
    def level_order(self):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:  # this case will work when the given value(deletion value) equals the traversal node ,also there are 3
            # cases the node is a leaf node ,it is a parent with left child or right child.
            if not current_node.left and not current_node.right:  # ensures that it is a leaf node
                return None
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            # this is the last case which the deletion node has two child
            max_left_node = self.find_max_node(current_node.left)
            current_node.value = max_left_node.value
            current_node.left = self.__delete_node(current_node.left, max_left_node.value)
        return current_node

    def delete(self, value):
        self.root = self.__delete_node(self.root, value)

    # to find maximum node on the left side of that particular node.maximum is present at the right of a node(right
    # child is greater).
    def find_max_node(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node


tree = BinaryST()
tree.insert(2)
tree.insert(1)
tree.insert(3)

tree.level_order()

tree.delete(1)
print('\n after deletion: ')
tree.level_order()
