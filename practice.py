import subprocess

def execute_command(command):
    try:
        # Introducing a command injection vulnerability
        result = subprocess.check_output(command, shell=True, encoding="utf-8")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

# Simulating untrusted user input
user_input = "echo Hello, this is a potential vulnerability!"
result = execute_command(user_input)

if result is not None:
    print(f"Command output: {result}")

