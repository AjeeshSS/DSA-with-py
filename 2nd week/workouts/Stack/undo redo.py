# implementing undo redo

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

    def undo(self):
        x = self.pop()
        st2.push(x)

    def redo(self):
        r = st2.pop()
        st1.push(r)


st1 = Stack()
st2 = Stack()
st1.push(5)
st1.push(78)
st1.push(67)
st1.push(34)
st1.print_stack()
print('\n')

st1.undo()
st1.undo()
st1.undo()

print('after undo')
st1.print_stack()
print('\n undo stack')
st2.print_stack()

print('\n after redo')
st2.redo()
st1.print_stack()
