import heapq

def prim(graph):
    min_spanning_tree = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(cost, start_vertex, neighbor) for neighbor, cost in graph[start_vertex]]

    heapq.heapify(edges)

    while edges:
        cost, src, dest = heapq.heappop(edges)
        if dest not in visited:
            visited.add(dest)
            min_spanning_tree.append((src, dest, cost))
            for neighbor, cost in graph[dest]:
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, dest, neighbor))

    return min_spanning_tree

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

# Find the minimum spanning tree using Prim's algorithm
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
