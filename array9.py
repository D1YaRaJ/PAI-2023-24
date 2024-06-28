#rotating array to right

array = [1, 2, 3, 4, 5]
print("Original array:", array)

n = len(array)
k = 2  # Number of rotations

rotated_array = array[-k:] + array[:-k]

print("Rotated array:", rotated_array)
