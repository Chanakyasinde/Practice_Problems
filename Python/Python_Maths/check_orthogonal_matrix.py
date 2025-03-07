def is_orthogonal(n, matrix):
    transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
    result = [[sum(matrix[i][k] * transpose[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j and result[i][j] != 1:
                return False
            elif i != j and result[i][j] != 0:
                return False
    
    return True

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if is_orthogonal(n, matrix):
    print("True")
else:
    print("False")
