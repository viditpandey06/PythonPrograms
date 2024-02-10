def count_paths(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a 2D dp array to store the number of paths
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the number of paths for the first row and first column
    for i in range(rows):
        dp[i][0] = 1
    for j in range(cols):
        dp[0][j] = 1
    
    # Fill the dp array using dynamic programming
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The value at the bottom-right corner of the dp array represents the total number of paths
    return dp[rows-1][cols-1]

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print("Total number of paths:", count_paths(matrix))
