def non_tailed_factorial(n):
    if n == 0:
        return 1
    else:
        result = n * non_tailed_factorial(n - 1)
        print(f"Intermediate result for {n}: {result}")
        return result

# Example usage
number = 5
print(f"Factorial of {number}: {non_tailed_factorial(number)}")
