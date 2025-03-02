import math

def count_balanced_binary_strings(N):
    if N % 2 != 0:
        return 0
    k = N // 2
    return math.comb(2 * k, k)

N = int(input().strip())
print(count_balanced_binary_strings(N))
