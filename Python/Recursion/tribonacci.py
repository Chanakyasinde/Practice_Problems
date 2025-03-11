def tri(n):
    # Write your code here
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return tri(n-1)+tri(n-2)+tri(n-3)
