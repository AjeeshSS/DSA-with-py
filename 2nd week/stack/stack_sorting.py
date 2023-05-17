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

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def sort(self):
        buffer = Stack()  # Create a Stack object for buffer
        buffer.push(self.top.value)
        self.top = self.top.next
        while self.top is not None:
            temp = self.top
            self.top = self.top.next
            while buffer.top is not None and buffer.top.value > temp.value:
                popped = buffer.top
                buffer.top = buffer.top.next
                popped.next = self.top
                self.top = popped
            temp.next = buffer.top
            buffer.top = temp
        self.top = buffer.top


my_stack = Stack()

print('\noriginal stack is:')
my_stack.print_stack()
print('Height is : ', my_stack.height)

arr = [3, 5, 2, 6]
for i in arr:
    my_stack.push(i)

print('\nafter push')
print('Height is : ', my_stack.height)
my_stack.print_stack()

print('\n after sort')
my_stack.sort()
my_stack.print_stack()

"""The sort() method in the Stack class is responsible for sorting the elements in the stack in ascending order using 
a variation of the insertion sort algorithm. Here's a step-by-step explanation of the sort() method: 

1.Create a buffer stack: A new instance of the Stack class is created as the buffer stack, which will be used to hold 
the sorted elements temporarily. 

2.Move the top element to the buffer stack: The top element of the original stack (self.top) is moved to the buffer 
stack using the push() method. This is done to initiate the sorting process. 

3.Iterate through the remaining elements in the original stack: Starting from the next element (self.top.next), 
iterate through the remaining elements of the original stack. 

4.Find the correct position in the buffer stack: For each element in the original stack, compare it with the elements 
in the buffer stack, starting from the top. Move elements from the buffer stack to the original stack (self.top) if 
they are greater than the current element, in order to make space for the current element. 

5.Insert the current element into the buffer stack: Once the correct position is found in the buffer stack, 
insert the current element at that position by updating the next pointers. 

6.Repeat steps 3-5 until all elements are sorted: Repeat steps 3-5 until all elements in the original stack are 
sorted and moved to the buffer stack. 

7.Update the top of the original stack: After the sorting is complete, update the top of the original stack (
self.top) with the top of the buffer stack (buffer.top), effectively transferring the sorted elements back to the 
original stack. 

8.Printing the sorted stack: Finally, you can call the print_stack() method to display the elements in the sorted stack.
"""