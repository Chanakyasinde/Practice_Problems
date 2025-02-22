n=int(input())
mat=[]
for c in range (n):
    lst=list(map(int,input().split()))
    mat.append(lst)

for i in range(n):
    for j in range(n):
        if(i>j):
            print(0,end=" ")
        else:
            print(mat[i][j],end=" ")
    print()
print()

for i in range(len(mat)):
    for j in range(len(lst)):
        if i<j:
            print(0,end=" ")
        else:
            print(mat[i][j],end=" ")
    print()
