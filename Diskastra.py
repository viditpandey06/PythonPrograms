import heapq

def dijkstra(graph, start):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to store vertices and their distances
    pq = [(0, start)]

    while pq:
        # Pop the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)

        # Skip if the current distance is greater than the known distance
        if current_distance > distances[current_vertex]:
            continue

        # Update distances to adjacent vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # If new distance is smaller, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Start vertex for Dijkstra's algorithm
start_vertex = 'A'

# Run Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from", start_vertex + ":", shortest_distances)
