def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j
        if i != min:  # if there is any change in min then only swap.
            arr[i], arr[min] = arr[min], arr[i]


arr1 = [64, 34, 25, 12, 22, 11, 90, 89]
selection_sort(arr1)
print(arr1)
# bubble ,selection,insertion sort all have O(n^2) time complexity
# bubble ,selection,insertion sort all have O(1) space complexity
# only insertion sort is O(n) time complexity if you start with a sorted (or almost sorted array)
