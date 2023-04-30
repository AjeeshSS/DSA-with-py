# for BST lookup(), insert(), remove() : complexity = O(log n)
# when tree is like a LL then : lookup(),remove() : complexity = O(n)
#  for insert() = O(1)
# ie inserting in LL is efficient

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryST:
    def __init__(self):
        self.root = None


tree = BinaryST()
print(tree.root)
# a binary tree with maximum number of nodes called full binary tree.
#  if there are no missing element it will be complete tree.
