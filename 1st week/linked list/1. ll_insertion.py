"""
common functions

def__init__(self,value)   create a node
def append(self,value)  create node and add at end  O(1)
def prepend(self,value) create node and add at beginning O(1)
def insert(self,index,value)  create node and add at specific index
"""


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
        """  complexity =  O(1) to add at end 
         remove an item at end O(n) because it need iteration all over to reset tail"""


ll1 = Linked_list(90)
ll1.append(78)
ll1.append(656)
ll1.append(56)
ll1.print_list()

# in normal case, insertion  take place on back only
