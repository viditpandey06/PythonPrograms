def divide(a, b):
    try:
        result = a / b
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Division operation completed.")

# Example usage:
numerator = 10
denominator = 0

divide(numerator, denominator)
