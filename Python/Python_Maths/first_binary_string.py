def count_binary_strings(n):
    if n<2:
        return 0

    return 2 ** (n-2)

n = int(input())
result = count_binary_strings(n)
print(result)
