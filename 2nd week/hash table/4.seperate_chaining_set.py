"""when a collision occurs (i.e., two keys are hashed to the same location), you don't want to overwrite the existing
item. Instead, you create a linked list (like a chain) in that compartment and add your item to the end of the list."""


class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    # adding values by separate chaining
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = [[key, value]]
        else:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    self.data_map[index][i][1] += value  # i used + here for adding else it replaces the existing value.
                    return
            self.data_map[index].append([key, value])

    """easy code for separate chaining. The output of both these are different."""
    # def set_item(self, key, value):
    #     index = self.__hash(key)
    #     if self.data_map[index] is None:
    #         self.data_map[index] = []
    #     self.data_map[index].append([key, value])


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 500)
my_hash_table.set_item('washers', 1500)
my_hash_table.set_item('nails', 1034)

my_hash_table.print_table()
