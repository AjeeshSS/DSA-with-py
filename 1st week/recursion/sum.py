def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)


print(sum_recursive(5))
# 1+2+3+4+5 = 15
