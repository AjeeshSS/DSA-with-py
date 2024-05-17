"""you are given an array of strings names, and an array heights
that consists of distinct positive integers.
both arrays are of length n. for each index i,names[i] and height[i]
denote the name and height of the ith person.
Return names sorted in ascending order by the people's height. """


def sort(arr1, arr2):
    n = len(arr2)
    for i in range(n - 1):
        temp = arr2[i]
        swap = arr1[i]
        j = i - 1
        while temp < arr2[j] and j > -1:
            arr2[j + 1] = arr2[j]
            arr1[j + 1] = arr1[j]
            arr2[j] = temp
            arr1[j] = swap
            j -= 1
    return arr1, arr2


names = ["manu", "Danny", "Harry"]
heights = [180, 165, 170]
print(sort(names, heights))
