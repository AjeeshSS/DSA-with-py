#Adding an element at the start of the DLL O(1)

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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


my_double_list = DoublyLL()
arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
for i in arr1:
    my_double_list.append(i)

print('length is :', my_double_list.length)
my_double_list.print_list()

print('\n after adding')
my_double_list.prepend(1)
print('\nlength is :', my_double_list.length)
my_double_list.print_list()
