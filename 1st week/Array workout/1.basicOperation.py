import array

arr = array.array('i', [1,2,3,4,5,6])

print("The created array is : ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")


print ("the index of 1st occurrence of 2 is : ", end="")
print (arr.index(2))
print("\r")


arr.reverse()
print("The array after reversing is : ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")
print("\r")