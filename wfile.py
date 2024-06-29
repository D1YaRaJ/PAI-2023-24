#write to a file
filename = "example1.txt"
content = "Hello, world!\nThis is a test file."

with open(filename, 'w') as file:
    file.write(content)

print(f"Content written to {filename}.")
