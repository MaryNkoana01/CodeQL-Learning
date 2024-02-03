def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

result = divide_numbers(10, 2)

if result is not None:
    print(f"The result is: {result}")

