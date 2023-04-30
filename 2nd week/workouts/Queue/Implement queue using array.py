# Implement queue using array

# Enqueue, Dequeue and Display elements in Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self):
        if self.first is None:
            print("empty queue")
        else:
            temp = self.first
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def enq(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def deq(self):
        if self.first is None:
            return
        temp = self.first
        if self.first.next is not None:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
            return temp


q1 = Queue()
arr = [5, 7, 3, 9]
for i in arr:
    q1.enq(i)

q1.print_queue()
