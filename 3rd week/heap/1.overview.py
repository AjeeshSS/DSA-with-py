"""

YouTube channel link to study algorithm: https://youtu.be/HqPJF2L5h9U (Abdul Bari)
must watch above channel

if a node is at index i
    then left child = 2*i+1 (if the array starts with 0th index)
    right child = 2*i+2  () (if the array starts with 0th index)
    parent = (i-1)%2  (if the array starts with 0th index) .(round the mode value inorder to get rounded to integer value)

a binary tree with maximum number of nodes called full binary tree.
 if there are no missing element it will be complete tree.

heap is a complete binary tree. teo types - max amd  min heap.
max_heap : it is a complete binary tree. root  will have the largest value. every
            parent node has a value greater than its child node.(duplicates allowed)
            complexity for creating and delete all :  O(n log n).
              for insert and deletion : O(log n).

min_heap : it is a complete binary tree. root  will have the smallest value . every
            parent node has a value smaller than its child node.(duplicates allowed)
            complexity for creating delete all :  O(n log n).
            for insert and deletion : O(log n).

we can also create it by O(n) using heapify method.

#  heap-sort in included inside min and max heap.
"""
