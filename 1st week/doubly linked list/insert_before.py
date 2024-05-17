# Insert a node before a node with x data


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

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
        return True

    def insert_before(self, val, x):
        new_node = Node(x)
        if self.head.value == val:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next.value != val:
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node


my_double_list = DoublyLL()
arr1 = [2, 3, 4, 5, 6]
for i in arr1:
    my_double_list.append(i)

my_double_list.print_list()
print()
print('after adding')
my_double_list.insert_before(5, 9)
my_double_list.print_list()
