#sum of each row and column
rows, cols = 3, 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

row_sums = [sum(row) for row in matrix]
col_sums = [sum(matrix[i][j] for i in range(rows)) for j in range(cols)]

print("Row sums:", row_sums)
print("Column sums:", col_sums)
