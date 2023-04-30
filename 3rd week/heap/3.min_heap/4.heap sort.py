class MinHeap:
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
            self.min_heapify(i)

    def min_heapify(self, i):
        n = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    # max heap sorts elements in descending order
    def heap_sort(self):
        min_sorted_arr = []
        n = len(self.heap)
        for i in range(n - 1, -1, -1):
            self.swap(0, i)
            min_sorted_arr.append(self.heap.pop())
            self.min_heapify(0)
        min_sorted_arr.reverse()
        return min_sorted_arr


arr = [4, 12, 7, 3, 9, 8, 5, 6]
my_min_heap = MinHeap()
my_min_heap.build_heap(arr)
print(my_min_heap.heap)

sorted_arr = my_min_heap.heap_sort()
print('\n after deletion : ', sorted_arr)
