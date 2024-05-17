def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return "not found"


arr = [4, 7, 2, 1, 5]
x = int(input("enter value to be searched: "))
result = linear_search(arr, x)
print("element position : ", result)  # Output: 2

# time complexity O(n) and space  complexity is : O(1)