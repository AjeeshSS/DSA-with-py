# replace a value with new value.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # printing the doubly linked list
    def print_list(self):
        if self.head is None:
            print("LL is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, end=' ')
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:  # search on first half of length.
            for _ in range(index):
                temp = temp.next
        else:   # search from backwards.
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
            
    

my_double_list = DoublyLL()
arr1 = [7, 9, 6, 8]
for i in arr1:
    my_double_list.append(i)

print('DLL :') 
my_double_list.print_list()

my_double_list.set_value(2, 10)
print('\n \n New DLL :') 
my_double_list.print_list()