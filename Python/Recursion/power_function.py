def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = int(input())  # base
n = int(input())  # exponent

print(power(x, n))
