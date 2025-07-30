arr=list(map(int, input().split()))
n=len(arr)
prefix=[0]*n
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]

k=int(input())
for _ in range(k):
    l,r=map(int, input().split())
    if l==0:
        print(prefix[r])
    else:
        print(prefix[r]-prefix[l-1])
