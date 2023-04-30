def change(str, key):
    newKey = key % 26
    newArr = []

    for i in range(len(str)):
        letterPosition = ord(str[i]) + newKey
        if letterPosition <= 122:
            char = chr(letterPosition)
            newArr.append(char)
        else:
            char = chr(96 + letterPosition % 122)
            newArr.append(char)

    return "".join(newArr)


print(change("Hello", 3))  # Output: Khoor
