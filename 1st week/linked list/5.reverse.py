# reverse the LL

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

    def reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        self.head = prev

    #         this reverse set the head to the end of the code

    # another method is
    def reversee(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = Linked_list(90)

arr = [78, 656, 56]
for i in arr:
    my_linked_list.append(i)
my_linked_list.print_list()
print()
print('after reverse')
my_linked_list.reverse()
my_linked_list.print_list()


# print('\n after reverse using second method')
# my_linked_list.reversee()
# my_linked_list.print_list()

