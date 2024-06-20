import array as arr


arr= arr.array('i', [1,2,3,4,5])
print("The new created array is : ", end='')
for i in range(0, 5):
    print(arr[i], end=' ')
print("\r")


print("The popped element is : ", end='')
print(arr.pop(2)) # pop element @ 2nd position
print("The array after popping is :", end='')
for  i in range(len(arr)):
    print(arr[i], end=' ')
print("\r")


arr.remove(1) # remove particular element
print("The array after removing is : ", end='')
for i in range(len(arr)):
    print(arr[i], end=' ')
print("\r")
