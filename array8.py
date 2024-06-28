#checking sorted array

array = [1, 2, 3, 4, 5]
print("Array:", array)

is_sorted = True
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        is_sorted = False
        break

print("Is array sorted?:", is_sorted)
