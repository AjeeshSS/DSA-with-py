arr = [1, 2, 3, 4, 5]
n = len(arr)

for i in range(n//2):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

print(arr)

'''Note that we use integer division (//) to ensure that 
we don't try to swap the middle element with itself in the
 case where the length of the array is odd.'''