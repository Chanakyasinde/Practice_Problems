n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
p1=0
p2=0
result=[]
while p1<n and p2<m:
    if arr1[p1]<=arr2[p2]:
        result.append(arr1[p1])
        p1+=1
    else:
        result.append(arr2[p2])
        p2+=1
while p1<n:
    result.append(arr1[p1])
    p1+=1
while p2<m:
    result.append(arr2[p2])
    p2+=1
print(*result)

# time space and total complexity i = o(n+m)
