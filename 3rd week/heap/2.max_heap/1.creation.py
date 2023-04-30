# here we build a heap.
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
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        n = len(self.heap)
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)


arr = [4, 1, 7, 3, 9, 2, 8, 5, 6]
my_max_heap = MaxHeap()
my_max_heap.build_heap(arr)
print(my_max_heap.heap)
