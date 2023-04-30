# Remove node  by value

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

    def delete_by_value(self, val):
        temp = self.head
        if temp.value == val:
            self.head = temp.next
            return

        while temp.next is not None:
            if temp.next.value == val:
                temp.next = temp.next.next
                return

            temp = temp.next
        print("The values not present")


my_linked_list = Linked_list(90)

arr = [78, 656, 56]
for i in arr:
    my_linked_list.append(i)
my_linked_list.print_list()
print()
my_linked_list.delete_by_value(656)
my_linked_list.print_list()
