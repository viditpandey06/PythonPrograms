# Using memoization to store calculated results
memo = {}

def non_tailed_factorial(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    else:
        result = n * non_tailed_factorial(n - 1)
        memo[n] = result
        print(f"Intermediate result for {n}: {result}")
        return result

# Example usage
number = 5
print(f"Factorial of {number}: {non_tailed_factorial(number)}")
