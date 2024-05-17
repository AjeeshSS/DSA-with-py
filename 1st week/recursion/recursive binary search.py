def binary_search(arr, low, high, target):
    # Base case: target not found in array
    if low > high:
        return -1

    # Calculate the midpoint of the array
    mid = (low + high) // 2

    # Check if target is at midpoint
    if arr[mid] == target:
        return mid

    # If target is less than midpoint, search left half of array
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)

    # If target is greater than midpoint, search right half of array
    else:
        return binary_search(arr, mid + 1, high, target)


# Driver code
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element {target} is present at index {result} in {arr}")
else:
    print("Element is not present in array")

"""
arr - the sorted list of integers to be searched
low - the lower index of the sublist being searched
high - the higher index of the sublist being searched
target - the integer being searched for
The function returns the index of target in the arr list if it is present, or -1 if it is not.

The driver code creates an example arr list and a target integer, and calls binary_search with the 
initial low index of 0, the initial high index of len(arr) - 1, and the target integer. It then 
prints out whether or not the target element was found in the list, and if so, at which index.
"""
