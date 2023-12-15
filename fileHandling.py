# File handling: Reading from a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# File handling: Writing to a file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to {file_name} successfully.")
    except PermissionError:
        print(f"No write permission to '{file_name}'.")

# Example usage:
file_name = "example.txt"
content_to_write = "Hello, this is a sample text."

# Write content to a file
write_to_file(file_name, content_to_write)

# Read content from a file
read_file(file_name)
