#display matrix
rows = 3
cols = 3
matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
