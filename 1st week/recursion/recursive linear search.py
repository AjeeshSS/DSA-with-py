def linear_search(arr, target):
    """
    Recursive linear search function that searches for the target element in the given array
    """
    # Base case: if the array is empty or the target element is not found, return -1
    if len(arr) == 0:
        return -1

    # Check if the first element is the target
    if arr[0] == target:
        return 0

    # Recursively search the remaining elements of the array
    sub_result = linear_search(arr[1:], target)

    # If the target is found in the subarray, adjust the result index accordingly
    if sub_result == -1:
        return -1
    else:
        return sub_result + 1


arr = [5, 3, 8, 4, 2, 1]
target = 4

# Call the linear_search() function and print the result
result = linear_search(arr, target)
if result == -1:
    print(f"{target} not found in {arr}")
else:
    print(f"{target} found at index {result} in {arr}")

"""
This function takes in an array arr and a target element target. The function first checks if the array is empty 
or if the target element is not found in the array. If either of these conditions is true, the function returns -1 
to indicate that the target element was not found.If the target element is found in the first element of the array,
 the function returns the index 0. Otherwise, the function recursively calls itself with the remaining elements of the 
 array (i.e., arr[1:]) and the same target element.The recursive call returns the index of the target element in
  the subarray, or -1 if the target element is not found. If the target element is found in the subarray, the
   function adjusts the result index by adding 1 to account for the fact that the subarray starts at 
   index 1 of the original array.Note that while recursive functions can be elegant and intuitive, they can also
    be less efficient than iterative solutions, especially for very large arrays.
"""
