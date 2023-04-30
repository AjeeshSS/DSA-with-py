#  fibonacci series of 5 is  0, 1, 1, 2, 3

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=' ')


print(fibonacci(10))  # Output: 55
print_fibonacci(10)  # Output: 0 1 1 2 3 5 8 13 21 34
