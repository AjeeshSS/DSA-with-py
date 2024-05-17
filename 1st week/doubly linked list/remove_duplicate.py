# Remove duplicate elements

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

        # deleting duplicate elements in the doubly linked list

    def delete_duplicate(self):
        if self.head is None:
            return

        values = set()
        current = self.head

        while current is not None:
            if current.value not in values:
                values.add(current.value)
                current = current.next
            else:
                next_node = current.next
                self._delete_node(current)
                current = next_node

    # helper function to delete a node
    def _delete_node(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev


my_double_list = DoublyLL()
arr1 = [2, 2, 3, 4, 4, 5, 5, 6, 6]
for i in arr1:
    my_double_list.append(i)

my_double_list.print_list()
print()
my_double_list.delete_duplicate()
my_double_list.print_list()
