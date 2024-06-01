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

    # it traverses through the tree
    def level_order(self):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


tree = BinaryST()
arr = [47, 21, 76, 18, 27, 52, 82]
for i in arr:
    tree.insert(i)

tree.level_order()

# these are types of traversal methods.
# 1. DFS methods: 1.1 preorder,1.2 postorder,1.3 inorder
# 2. BFS method: level order(BFS is also known as level order).

'''
there are 2 types of serch in BST, they are BFS (Level Order) and DFS (In-order, Pre-order, Post-order).
there are three primary methods to visit all the nodes in a specific order: inorder, preorder, and postorder traversal. Each method visits nodes in a unique sequence, useful for different purposes such as tree reconstruction or obtaining a specific order of elements.

Inorder Traversal (Left, Root, Right)
In inorder traversal, nodes are visited in the following sequence:

Visit the left subtree.
Visit the root node.
Visit the right subtree.
Usage: Inorder traversal is particularly useful for binary search trees (BSTs) because it visits nodes in ascending order, thus retrieving sorted elements.

Preorder Traversal (Root, Left, Right)
In preorder traversal, nodes are visited in the following sequence:

Visit the root node.
Visit the left subtree.
Visit the right subtree.
Usage: Preorder traversal is useful for creating a copy of the tree, or for generating a prefix expression (Polish notation) of an expression tree.

Postorder Traversal (Left, Right, Root)
In postorder traversal, nodes are visited in the following sequence:

Visit the left subtree.
Visit the right subtree.
Visit the root node.
Usage: Postorder traversal is useful for deleting nodes in a tree (as nodes are deleted only after their children) or for generating a postfix expression (Reverse Polish notation) of an expression tree.

Summary of Differences
Inorder: Visits nodes in the sequence of left subtree, root, right subtree. It is used to get nodes in non-decreasing order in a BST.
Preorder: Visits nodes in the sequence of root, left subtree, right subtree. It is used for copying trees and prefix expressions.
Postorder: Visits nodes in the sequence of left subtree, right subtree, root. It is used for deleting trees and postfix expressions.
'''

"""
study complexity of BFS  and DFS
"""