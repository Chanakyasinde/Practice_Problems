def trailingZeroes(N):
    if N<5:
        return 0
    else:
        return N//5+trailingZeroes(N//5)
