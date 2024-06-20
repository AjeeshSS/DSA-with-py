def changes (s, key):
    new_key = key % 26
    new_arr = []
    
    for i in range(len(s)):
        letter_positions = ord(s[i]) + new_key
        if letter_positions <= 122:
            char = chr(letter_positions)
            new_arr.append(char)
        else:
            char = chr(96 + letter_positions % 122)
            new_arr.append(char)
            
    return new_arr
    
print(changes("Hello", 3))
# encode the string using a key.