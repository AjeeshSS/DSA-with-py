# Add node at the end

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

    def add_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        """  complexity =  O(1) to add at end"""


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.print_list()
print()
ll1.add_end(105)
print('after adding')
ll1.print_list()

# in normal case, insertion  take place on backside(tail) only so both 'append' and 'add_end' code are same
