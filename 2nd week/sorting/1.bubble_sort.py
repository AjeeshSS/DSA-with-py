def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #swapping


if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    bubbleSort(arr)
    print(arr)


# Optimized program

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # if swapped == False:
            break


arr1 = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr1)
print('\n', arr1)

# bubble ,selection,insertion sort all have O(n^2) time complexity
# bubble ,selection,insertion sort all have O(1) space complexity
# only insertion sort is O(n) time complexity if you start with a sorted (or almost sorted array)
# merge sort, quick sort have O(nlogn) time complexity
# merge sort have O(n) space complexity
# quick sort have O(logn) space complexity


