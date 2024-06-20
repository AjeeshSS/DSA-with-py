import array


arr = array.array('i', [1,2,3])
print ("The created array is : ", end='')
for i in range(len(arr)):
    print (arr[i], end=' ')
print ("\r")


arr.append(4)
print ("The appended array is : ", end='')
for  i in range(len(arr)):
    print (arr[i], end=' ')
print ("\r")

# add 5 to the position 2
arr.insert(2, 5) 
print ("The array after insertion is : ", end='')
for i in range(len(arr)):
    print (arr[i], end=' ')
print ("\r")
