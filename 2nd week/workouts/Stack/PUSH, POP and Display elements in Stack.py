#  PUSH, POP and Display elements in Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def print_stack(self):
        if self.top is None:
            print('empty stack')
        else:
            temp = self.top
            while temp is not None:
                print(temp.value, '\n\u2193')
                temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1
        return temp.value


st1 = Stack()
st1.push(51)
st1.push(93)
st1.push(65)

st1.pop()
st1.pop()

st1.print_stack()
