def Sum(N):
    if N==0:
        return 0
    return (N%10) + Sum(N//10)
