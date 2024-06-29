#inverse
rows, cols = 2, 2
matrix = []

print("Enter 2x2 matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

if det == 0:
    print("Matrix is singular, inverse does not exist.")
else:
    inverse = [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det]
    ]
    print("Inverse matrix:")
    for row in inverse:
        print(" ".join(map(str, row)))
