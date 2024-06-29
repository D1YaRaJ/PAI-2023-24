#symmetric matrix
rows, cols = 3, 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

is_symmetric = all(matrix[i][j] == matrix[j][i] for i in range(rows) for j in range(cols))

print("Is matrix symmetric?:", is_symmetric)
