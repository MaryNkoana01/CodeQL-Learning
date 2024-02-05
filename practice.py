def read_file_content(file_name):
    try:
        # Introducing a path traversal vulnerability
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Simulating untrusted user input
user_input = "../secret_file.txt"
result = read_file_content(user_input)

if result is not None:
    print(f"The file content is: {result}")
