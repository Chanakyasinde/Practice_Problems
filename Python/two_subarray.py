n=int(input())
lst=list(map(int, input().split()))
for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(lst[k],end=" ")
        print()
