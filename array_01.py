n = int(input())
m = int(input())
multi_array= [];

for i in range(n):
    row  = [1] * m
    multi_array.append(row)
    for j in range(m):
        multi_array[i][j] = int(input())

def zeroMatrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):a
                for k in range(m):
                    matrix[i][k] = 0
                for l in range(n):
                    matrix[l][j] = 0
    return matrix
matrix = zeroMatrix(multi_array,n,m)
