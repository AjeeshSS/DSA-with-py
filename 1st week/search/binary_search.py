def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 3, 5, 7, 9]
x = int(input("enter value to be searched: "))

index = binary_search(arr, x)

if index != -1:
    print(f"{x} found at index {index}")
else:
    print(f"{x} not found in the array")

# time complexity O(log n) and space  complexity is : O(1)