#remove duplicates

array = [1, 2, 3, 2, 4, 2, 5, 1, 5]
print("Original array:", array)

unique_array = []
for num in array:
    if num not in unique_array:
        unique_array.append(num)

print("Array without duplicates:", unique_array)
