# Insert a node before a node with x data

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.value, end=",")
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert_before(self, val, x):
        new_node = Node(x)
        if self.head.value == val:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next.value != val:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        """ for adding complexity = O(n)
         for removing  O(n)"""


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.print_list()
print()
print('after insertion')
ll1.insert_before(56, 5)
ll1.print_list()

# in normal case, insertion  take place on back only
