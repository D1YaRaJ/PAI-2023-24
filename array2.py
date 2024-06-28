#array min element
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_element = array[0]

for num in array:
    if num < min_element:
        min_element = num

print("Array:", array)
print("Minimum element:", min_element)
