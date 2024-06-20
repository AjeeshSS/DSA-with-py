string = "hello world"
index = 6
substring = "there"
nstring = string[:index] + substring + string[index:]
print(nstring)


str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)


my_string = "Hello"
front_value = "Hi"
back_value = "!"
result = front_value + my_string + back_value
print(result)


my_string = "Hello"
front_value = "Hi"
back_value = "!"
result = f"{front_value}{my_string}{back_value}"
print(result)
