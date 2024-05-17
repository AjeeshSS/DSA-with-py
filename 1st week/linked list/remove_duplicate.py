# Remove duplicate elements

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

    def delete_duplicate(self):
        if self.head is None:
            return

        # create a set to keep track of values
        seen_values = set()

        # traverse the linked list
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value in seen_values:
                # delete current node
                prev.next = curr.next
            else:
                # add current value to the set and move to next node
                seen_values.add(curr.value)
                prev = curr
            curr = curr.next


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.append(78)
print('Original list:')
ll1.print_list()
print('\nList after removing duplicates:')
ll1.delete_duplicate()
ll1.print_list()

