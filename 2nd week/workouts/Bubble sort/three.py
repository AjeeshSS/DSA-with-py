"""given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing
order. """


def sort(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 2

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


nums = [-4, -1, 0, 7, 47]
print(sort(nums))
