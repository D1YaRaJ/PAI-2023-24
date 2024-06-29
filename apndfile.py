#append to file
filename = "example1.txt"
new_content = "\nThis is an appended line."

with open(filename, 'a') as file:
    file.write(new_content)

print(f"New content appended to {filename}.")
