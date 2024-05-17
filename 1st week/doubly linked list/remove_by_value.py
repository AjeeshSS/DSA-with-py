# Remove elements by value

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
        print("The value is not present")


my_double_list = DoublyLL()
arr1 = [1, 2, 3, 4, 5, 6]
arr1 = [1, 2, 3, 4, 5, 6]
for i in arr1:
    my_double_list.append(i)

my_double_list.print_list()
print()
print('after delete')
my_double_list.delete_by_value(4)
my_double_list.print_list()
