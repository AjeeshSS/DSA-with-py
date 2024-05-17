#  search a value present or not

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

    def search_by_value(self, x):
        if self.head is None:
            print("Linked list is empty")

        elif self.head.value == x:
            return True
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                if x == temp.value:
                    return True
            return False


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.print_list()

print()

print(ll1.search_by_value(565))


