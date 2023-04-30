""" given two arrays arr1 and arr2 , the elements of arr2 are distinct,
and  all elements in the arr2 are also in arr1 .
sort the elements of arr1 such that the relative ordering of items in arr1
are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in
ascending order.   """


def sort(arr1, arr2):
    for i in arr2:
        if i not in arr1:
            arr1.append(i)

    n = len(arr1)
    for i in range(1, n):
        temp = arr1[i]
        j = i - 1
        while temp < arr1[j] and j > -1:
            arr1[j + 1] = arr1[j]
            arr1[j] = temp
            j -= 1
    return arr1


arr1 = [1, 4, 7, 6, 3, 9]
arr2 = [11, 4, 78, 64, 3, 9]
print(sort(arr1, arr2))
