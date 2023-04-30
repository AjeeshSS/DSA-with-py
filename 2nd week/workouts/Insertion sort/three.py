"""given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing
order. """


def sort(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 2

    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j > -1:
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr


nums = [-4, -1, 0, 7, 8]
print(sort(nums))
