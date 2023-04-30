# search by value


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

    def search_by_value(self, x):

        if self.head is None:
            print(True)

        elif self.head.value == x:
            print(True)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                if x == temp.value:
                    print(True)
                    return
            print(False)
            return


my_double_list = DoublyLL()
arr1 = [2, 3, 4, 5, 6]
for i in arr1:
    my_double_list.append(i)

my_double_list.print_list()
print()
my_double_list.search_by_value(5)
