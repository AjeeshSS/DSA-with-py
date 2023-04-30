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
arr = [1, 4, 2, 5, 8, 9]
for i in arr:
    st1.push(i)
st1.print_stack()
