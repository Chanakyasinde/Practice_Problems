k=int(input())
low=1
high=k
while low<=high:
    mid=(low+high)//2
    y=(2*mid*mid)+(5*mid)
    if y>k:
        high=mid-1
    elif y<k:
        low=mid+1
    else:
        print(mid)
        break
if high<low:
    print(-1)
