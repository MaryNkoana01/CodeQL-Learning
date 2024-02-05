import sqlite3

def divide_numbers(a, b):
    try:
        # Introducing a SQL injection vulnerability
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        cursor.execute(f"SELECT {a} / {b}")
        result = cursor.fetchone()[0]
        connection.close()
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

result = divide_numbers(10, 1)

if result is not None:
    print(f"The result is: {result}")
