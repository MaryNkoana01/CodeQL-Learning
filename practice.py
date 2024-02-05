def insecure_eval(input_data):
    try:
        # Introducing a code injection vulnerability
        result = eval(input_data)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

# Simulating untrusted user input
user_input = "__import__('os').system('echo This is a potential vulnerability!')"
result = insecure_eval(user_input)

if result is not None:
    print(f"Eval result: {result}")


