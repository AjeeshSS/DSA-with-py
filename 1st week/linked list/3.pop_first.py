# pop an item at head O(1)

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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:  # this is  works when there is only one node
            self.tail = None
        return temp   


my_linked_list = Linked_list(90)

arr = [78, 656, 56]
for i in arr:
    my_linked_list.append(i)
my_linked_list.print_list()
print('\n after pop')
my_linked_list.pop_first()
my_linked_list.print_list()

# in normal case, insertion  take place on back only
