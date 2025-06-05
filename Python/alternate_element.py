n=int(input())
arr=list(map(int,input().split()))
new = []
for i in range(0,n,2):
    new.append(arr[i])
print(*new)
