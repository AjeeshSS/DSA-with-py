class HashTable:
    def __init__(self, size=10):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = my_hash + ord(letter)
        return my_hash % len(self.data_map)

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    # getting item by linear probing
    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        else:
            i = index
            while self.data_map[i] is not None and self.data_map[i][0][0] != key:
                i = (i + 1) % len(self.data_map)
            if self.data_map[i] is None:
                return None
            elif self.data_map[i][0][0] == key:
                return self.data_map[i][0][1]
            else:
                return None

    # setting item by linear probing
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = [[key, value]]
        else:
            i = index
            while self.data_map[i] is not None and self.data_map[i][0][0] != key:
                i = (i + 1) % len(self.data_map)
            if self.data_map[i] is None:
                self.data_map[i] = [[key, value]]
            elif self.data_map[i][0][0] == key:
                self.data_map[i][0][1] += value
            else:
                self.data_map[i].append([key, value])


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 500)
my_hash_table.set_item('washers', 1500)
my_hash_table.set_item('nails', 1034)

my_hash_table.print_table()

print('\n', my_hash_table.get('washers'))
