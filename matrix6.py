#determinant
rows, cols = 2, 2
matrix = []

print("Enter 2x2 matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

print("Determinant:", determinant)
