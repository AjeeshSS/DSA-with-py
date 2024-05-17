def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1


arr1 = [64, 34, 25, 12, 22, 11, 90, 89]
insertion_sort(arr1)
print(arr1)

# bubble ,selection,insertion sort all have O(n^2) time complexity
# bubble ,selection,insertion sort all have O(1) space complexity
# only insertion sort is O(n) time complexity if you start with a sorted (or almost sorted array)
