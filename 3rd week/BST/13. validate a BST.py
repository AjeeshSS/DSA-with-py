# check whether  left side of a tree contains value less than root and in right side the value is greater than root

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

    def level_order(self):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    #  the range is set to float('-inf') and float('inf'), which represent negative and positive infinity, respectively.
    # here we use binary search .
    def is_bst(self, root, min_value=float('-inf'), max_value=float('inf')):
        if root is None:
            return True

        if root.value < min_value or root.value > max_value:
            return False

        left_bst = self.is_bst(root.left, min_value, root.value - 1)
        right_bst = self.is_bst(root.right, root.value + 1, max_value)

        return left_bst and right_bst


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.level_order()
print('\n Is valid ? : ', tree.is_bst(tree.root))
