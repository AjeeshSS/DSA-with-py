def is_valid_parenthesis(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif not stack or stack.pop() != c:
            return False
    
    return not stack

string = input("Enter a string of patenthesis:")

if is_valid_parenthesis(string):
    print("The string is valid.")
else:
    print("The string is not valid.")
            
            