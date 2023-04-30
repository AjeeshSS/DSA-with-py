class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

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
# Mid Square Method.
# Folding Method.
# Multiplication Method.

# application = encryption - decription, cryptocurrency, cryptography
#  types of collition
# 1. Separate chaining
# 2. Open addressing -  Linear probing, Quadratic probing, Double hashing
# 3. Coalesced hashing
#   search pros and cons of hash table


