# for BST lookup(), insert(), remove() : complexity = O(log n) means height of tree (H) (when the tree is balanced)
# when tree is like a LL then eg(47,76,82,91 forms a LL rather than tree): lookup(),remove() : complexity = O(n)
#  for insert() = O(1)
# ie inserting in LL is efficient for insertion.

# study detail about height of a tree and balanced tree (theory).

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
# a binary tree with maximum number of nodes called full binary tree.(each node should be filled with 2 or none)
# a binary tree with a height contain all the nodes then that is perfect tree.
#  if there are no missing element it will be complete tree.
# first node is root , 2nd node is children, last node with no children called leaf node.
# binary search tree the node greater than root/parent will align to right and smaller than root/parent will align to left.
# height of a BST is 2^h-1

"""BSTs are used for a lot of applications due to its ordered structure. BSTs are used for indexing and multi-level 
indexing. They are also helpful to implement various searching algorithms. It is helpful in maintaining a sorted 
stream of data. """

"""Binary search trees (BSTs) have many applications in computer science and other fields. Here are some examples:

Searching: One of the main applications of BSTs is searching. BSTs provide an efficient way to search for a specific 
key in a collection of keys. The search operation in a BST has a time complexity of O(log n) in the average case and 
O(n) in the worst case. 

Sorting: BSTs can be used to sort a collection of keys. In-order traversal of a BST produces the keys in sorted 
order. However, the time complexity of sorting using a BST is O(n^2) in the worst case, which is not as efficient as 
other sorting algorithms like quicksort or merge sort. 

Indexing: BSTs can be used to implement indexing in databases or other data storage systems. Each record in the 
database can be represented as a key-value pair, where the key is used as the index. The BST provides efficient 
access to records based on their index. 

Symbol tables: BSTs can be used to implement symbol tables, which are used in compilers, interpreters, 
and other language processing systems. A symbol table maps symbols (e.g., variables, functions, classes) to their 
associated attributes (e.g., type, scope, value). 

Priority queues: BSTs can be used to implement priority queues, which are used in scheduling, resource allocation, 
and other applications where tasks need to be performed in a certain order. The priority queue stores tasks along 
with their priority, and tasks are executed in order of their priority. 

Huffman coding: BSTs can be used to implement Huffman coding, which is a compression algorithm used in data 
compression. Huffman coding assigns shorter codes to more frequent symbols in a data stream, and longer codes to less 
frequent symbols. A BST can be used to build the Huffman tree, which is used to generate the codes. """
