#  fibonacci series of 5 is  0, 1, 1, 2, 3
 
# Using recursion
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


# using memoization
memo = [None] * 100   
counter = 0

def fib (n):
    global counter
    counter += 1
    
    if memo [n] is not None: 
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n - 1) + fib(n - 2)
    
    return memo[n]

n=7 

print("fib of", n, '=',fib(n))
print("counter: ", counter)


# Another example
counter = 0

def fib (n):
    fib_list = [0, 1]
    global counter
    for index in range(2, n+1):
        counter += 1
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]

n = 7
print('Fib of', n, '=', fib(n))
print("counter: ", counter)
