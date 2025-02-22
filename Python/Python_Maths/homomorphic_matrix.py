n1,m1=map(int,input().split())
mat1=[]
for i in range(n1):
    l=list(map(int,input().split()))
    mat1.append(l)
n2,m2=map(int,input().split())
mat2=[]
for i in range(n2):
    o=list(map(int,input().split()))
    mat2.append(o)
if(n1!=n2 or m2!=m1):
    print(-1)
else:
    for i in range(n2):
        for j in range(m2):
            sum=mat1[i][j]+mat2[i][j]
            print(sum,end=" ")
        print()
