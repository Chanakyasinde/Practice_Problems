def transpose_matrix(n, m, matrix):
    transposed = [[matrix[i][j] for i in range(n)] for j in range(m)]
    for row in transposed:
        print(" ".join(map(str, row)))

n, m = map(int, input().split())  
matrix = [list(map(int, input().split())) for _ in range(n)]  
transpose_matrix(n, m, matrix)
