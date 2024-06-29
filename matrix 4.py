#matrix trace(sum of diagonal)
rows, cols = 3, 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

trace = sum(matrix[i][i] for i in range(min(rows, cols)))

print("Matrix trace:", trace)
