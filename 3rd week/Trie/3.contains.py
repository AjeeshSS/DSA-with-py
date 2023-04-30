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
        def traverse_trie(node, prefix):
            if node.isWordEnd:
                print(prefix)
            for char, child in node.children.items():
                traverse_trie(child, prefix + char)

        traverse_trie(self.root, '')

    # contains means search
    def contains(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWordEnd


t = Trie()
t.insert("Malayalam")
t.insert("Manu s pilla")
t.insert("Manikkam")
t.insert("Kiran")
t.insert("Kala")

t.print_trie()
print('\n', t.contains("Manu s pilla"))
