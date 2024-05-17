"""given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing
order. """


def sort(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 2

    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


nums = [-4, -1, 0, 7, 8]
print(sort(nums))
