n=int(input())
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
def matrix_type(n, matrix):
    is_diagonal = True
    is_symmetric = True
    is_skew_symmetric = True
    for i in range(n):
        for j in range(n):
            if i !=j and matrix[i][j] !=0:
                is_diagonal =False
            if matrix[i][j] !=matrix[j][i]:
                is_symmetric =False
            if matrix[i][j] !=-matrix[j][i]:
                is_skew_symmetric =False
            if i ==j and matrix[i][j] !=0:
                is_skew_symmetric =False
    if is_diagonal:
        return "Diagonal"
    elif is_symmetric:
        return "Symmetric"
    elif is_skew_symmetric:
        return "Skew-Symmetric"
    else:
        return "None"
final=matrix_type(n, matrix)
print(final)
