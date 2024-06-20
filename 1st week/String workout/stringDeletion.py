string = input("Enter a string: ")
char = input("Enter a character to delete: ")

# Check if the character is in the string
if char in string:
    new_string = string.replace(char, "")
    print("New string: ", new_string)
else:
    print("Character not found in the string: ", char)