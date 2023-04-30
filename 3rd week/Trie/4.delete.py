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

    def deleteHelper(self, curr, word, index):
        # This function recursively traverses the trie to find the node containing the last character of the given
        # word. It returns True if the node corresponding to the last character of the word has no children,
        # indicating that it can be safely deleted.

        if index == len(word):
            # If we have traversed to the last character of the word, we set the isWordEnd flag of the current node
            # to False, indicating that the word is no longer present in the trie.
            curr.isWordEnd = False
            # We then check if the current node has any children. If not, we can safely delete the current node and
            # return True.
            return len(curr.children) == 0

        # If we haven't traversed to the last character of the word yet,
        # we get the next character of the word and check if it exists in the current node's children.
        char = word[index]
        if char not in curr.children:
            # If the character is not found in the current node's children,
            # it means the word is not present in the trie, so we return False.
            return False

        # If the character is found in the current node's children,
        # we recursively call deleteHelper on the child node corresponding to the character.
        # The index is incremented by 1 to move to the next character of the word.
        shouldDeleteCurrentNode = self.deleteHelper(curr.children[char], word, index + 1)

        # If the child node corresponding to the last character of the word can be deleted,
        # we remove it from the current node's children and check if the current node has any other children.
        if shouldDeleteCurrentNode:
            del curr.children[char]
            # If the current node has no other children, it can be safely deleted.
            return len(curr.children) == 0

        # If the child node corresponding to the last character of the word cannot be deleted,
        # we return False, indicating that the current node should not be deleted.
        return False

    def delete(self, word):
        # This function is the public interface for deleting a word from the trie.
        # It calls the deleteHelper function with the root node and the word to be deleted.
        self.deleteHelper(self.root, word, 0)


t = Trie()
t.insert("Malayalam")
t.insert("Manu s pilla")
t.insert("Manikkam")
t.insert("Kiran")
t.insert("Kala")

t.print_trie()

t.delete("Kala")
t.delete("Manikkam")
print('\n after deletion : \n')
t.print_trie()
