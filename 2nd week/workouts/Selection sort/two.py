"""you are given an array of strings names, and an array heights
that consists of distinct positive integers.
both arrays are of length n. for each index i,names[i] and height[i]
denote the name and height of the ith person.
Return names sorted in ascending order by the people's height. """


def sort(arr1, arr2):
    n = len(arr2)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr2[min] > arr2[j]:
                min = j
        if i != min:
            arr2[i], arr2[min] = arr2[min], arr2[i]
            arr1[i], arr1[min] = arr1[min], arr1[i]
    return arr1, arr2


names = ["manu", "Danny", "Harry"]
heights = [180, 165, 170]
print(sort(names, heights))
