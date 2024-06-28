array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_element = array[0]

for num in array:
    if num > max_element:
        max_element = num

print("Array:", array)
print("Maximum element:", max_element)
