#read from file
filename = "example1.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Content of {filename}:")
        print(content)
except FileNotFoundError:
    print(f"{filename} not found.")
