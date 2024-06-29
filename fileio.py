def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

filename = "sample.txt"
content = "Hello, this is a sample file content."

write_to_file(filename, content)
print("Content written to file.")

read_content = read_from_file(filename)
print("Content read from file:")
print(read_content)
