import numpy as np
import numpy as np
import numpy as np
from collections import defaultdict

# Import the necessary libraries

# Define the Kahn algorithm for topological sorting of a graph
def kahn_algorithm(graph):
    # Initialize the in-degree of each vertex
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize the queue with nodes having in-degree 0
    queue = []
    for node in graph:
        if in_degree[node] == 0:
            queue.append(node)
    
    # Perform the topological sorting
    sorted_order = []
    while queue:
        node = queue.pop(0)
        sorted_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Run the Kahn algorithm
result = kahn_algorithm(graph)
print("Topological sorting order:", result)
print("Optimal solution:", result)

# Save the result to a file
with open('/c:/Users/Udit/OneDrive/Desktop/PythonPrograms/PythonPrograms/result.txt', 'w') as file:
    file.write(f"Minimum value found: {objective_function(result)}\n")
    file.write(f"Optimal solution: {result}\n")