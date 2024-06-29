#matrix diagonals
rows, cols = 3, 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_diagonal = [matrix[i][i] for i in range(min(rows, cols))]
secondary_diagonal = [matrix[i][cols - i - 1] for i in range(min(rows, cols))]

print("Primary diagonal:", primary_diagonal)
print("Secondary diagonal:", secondary_diagonal)
