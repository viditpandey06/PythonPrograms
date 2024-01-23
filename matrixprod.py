import numpy as np
import time

# Define the matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

# Perform matrix multiplication
start_time = time.time()
result = np.dot(A, B)
end_time = time.time()

# Print the result and total time taken
print("Result:")
print(result)
print("Total time taken:", end_time - start_time, "seconds")
