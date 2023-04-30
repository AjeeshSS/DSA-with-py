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

    def traverseHelper(self, node, word, words):
        if node.isWordEnd:
            words.append(word)
        for char, childNode in node.children.items():
            self.traverseHelper(childNode, word + char, words)

    def traverse(self):
        words = []
        self.traverseHelper(self.root, '', words)
        return words


t = Trie()
t.insert("Malayalam")
t.insert("Manu s pilla")
t.insert("Manikkam")
t.insert("Kiran")
t.insert("Kala")

t.print_trie()

print('\n', t.traverse())
