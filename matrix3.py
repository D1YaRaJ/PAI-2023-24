#multiply matrix
rows1, cols1 = 2, 2
rows2, cols2 = 2, 2
matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = []

print("Enter elements of second matrix row-wise:")
for i in range(rows2):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = [
    [0 for _ in range(cols2)] for _ in range(rows1)
]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Product of matrices:")
for row in result:
    print(" ".join(map(str, row)))
