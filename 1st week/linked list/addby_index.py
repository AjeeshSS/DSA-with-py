# add node by index O(n)

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

    def add_begin(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0: 
            return self.add_begin(value) # insert at head position
        if index == self.length:
            return self.append(value)  # insert at tail position
        new_node = Node(value) # insert at other position
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.print_list()

print('\n after insertion')
ll1.insert(3, 88)
ll1.print_list()
