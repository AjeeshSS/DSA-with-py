"""
A hash table, also known as a hash map, is a data structure that stores key-value pairs. It provides efficient
retrieval and insertion of data by using a hashing function."""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    # this is hash function, here I use the custom hash function
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    #  "ord(letter)" gives the ASCII value of letters and 23 is a prime number, and we can add any prime number.

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


my_hash_table = HashTable()
my_hash_table.print_table()

# Types of Hash functions::

# Division Method.
# Multiplication Method.
# Mid Square Method.
# Folding Method.

# application of hashtable = encryption - decryption, crypto currency, cryptography
"""Hash tables are commonly used to implement caching systems. Used in various cryptographic algorithms. 
Hash tables are used in load balancing algorithms.
We can use hash tables to store, retrieve, and delete data uniquely based on their unique key. """
#  types of collision handling methods.
# 1. Separate chaining
# 2. Open addressing -  Linear probing, Quadratic probing, Double hashing
# 3. Coalesced hashing
#   search pros and cons of hash table

"""wost case time complexity = O(1)"""
