array=list(map(int,input().split()))
n=len(array)
sub=[]
for i in range(n):
    for j in range(i,n):
        sub.append(array[i:j+1])
print(sub)
