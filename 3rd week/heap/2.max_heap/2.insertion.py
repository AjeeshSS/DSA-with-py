class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_heap(self, arr):
        # Initialize the heap with the input array
        self.heap = arr
        # Get the length of the heap
        n = len(self.heap)
        # Loop through each non-leaf node of the heap in reverse order
        for i in range(n // 2 - 1, -1, -1):
            # Apply max-heapify to the current node
            self.max_heapify(i)

    def max_heapify(self, i):
        # Get the length of the heap
        n = len(self.heap)
        # Initialize the largest element index as the current node index
        largest = i
        # Compute the index of the left child of the current node
        left = self.left_child(i)
        # Compute the index of the right child of the current node
        right = self.right_child(i)
        # Check if the left child is larger than the current node
        if left < n and self.heap[left] > self.heap[largest]:
            # Update the largest element index if necessary
            largest = left
            # Check if the right child is larger than the current largest element
        if right < n and self.heap[right] > self.heap[largest]:
            # Update the largest element index if necessary
            largest = right
            # Check if the largest element index has changed from the current node index
        if largest != i:
            # Swap the current node with the largest element
            self.swap(i, largest)
            # Recursively apply max-heapify to the new node index
            self.max_heapify(largest)

    def insert(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)


arr = [4, 1, 7, 3, 9, 2, 8, 5, 6]
my_max_heap = MaxHeap()
my_max_heap.build_heap(arr)
print(my_max_heap.heap)

my_max_heap.insert(20)
print('\n after insertion', my_max_heap.heap)
