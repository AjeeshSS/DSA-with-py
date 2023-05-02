# create, read, update, delete O(l) where l is the length.
"""A Trie is a special data structure used to store strings that can be visualized like a graph. It consists of nodes
and edges. Each node consists of at max 26 children and edges connect each parent node to its children. """


class Node:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.isWordEnd = True

    def print_trie(self):
        """
        This function prints out all the words in the trie.
        """

        # Define a recursive function that will be used to traverse the trie.
        def traverse_trie(node, prefix):
            # If we've reached the end of a word, print out the prefix.
            if node.isWordEnd:
                print(prefix)
            # Traverse all the child nodes and continue building the prefix.
            for char, child in node.children.items():
                traverse_trie(child, prefix + char)

        # Start the traversal at the root node with an empty prefix.
        traverse_trie(self.root, '')


t = Trie()
t.insert("Malayalam")
t.insert("Manu s pilla")
t.insert("Manikkam")
t.insert("Kiran")
t.insert("Kala")

t.print_trie()
