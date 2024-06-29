#transpose
rows, cols = 3, 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = [
    [matrix[j][i] for j in range(rows)]
    for i in range(cols)
]

print("Transposed matrix:")
for row in transpose:
    print(" ".join(map(str, row)))
