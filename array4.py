#median
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
array.sort()
n = len(array)
median = 0

if n % 2 == 0:
    median = (array[n//2 - 1] + array[n//2]) / 2
else:
    median = array[n//2]

print("Sorted array:", array)
print("Median:", median)

