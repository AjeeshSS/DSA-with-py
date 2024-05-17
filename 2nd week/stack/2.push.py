class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        if self.top is None:
            print('empty stack')
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def push(self, value): # complexity is O(1)
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


my_stack = Stack()

print('\noriginal stack is')
my_stack.print_stack()
print('Height is : ', my_stack.height)

my_stack.push(5)
my_stack.push(6)
print('\nafter push')
print('Height is : ', my_stack.height)
my_stack.print_stack()
