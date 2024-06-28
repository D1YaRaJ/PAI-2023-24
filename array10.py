#Finding the Second Largest Element
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
first = second = float('-inf')

for num in array:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Array:", array)
print("Second largest element:", second)
