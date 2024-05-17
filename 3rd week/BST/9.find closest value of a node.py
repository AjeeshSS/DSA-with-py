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

    def findClosestValue(self, root, target):
        closestValue = root.value
        minDiff = abs(root.value - target)

        def dfs(node):
            nonlocal closestValue, minDiff
            if not node:
                return
            diff = abs(node.value - target)
            if diff < minDiff:
                closestValue = node.value
                minDiff = diff
            if target < node.value:
                dfs(node.left)
            elif target > node.value:
                dfs(node.right)

        dfs(root)
        return closestValue


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.level_order()

print("The element is:\n", tree.findClosestValue(tree.root, 25))
