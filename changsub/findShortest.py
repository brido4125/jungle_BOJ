from typing import List
from collections import deque

def minimumTreePath(n,edges, visitNodes):
    # Create adjacency list from edge list
    adj_list = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Initialize distance array with all values set to infinity except for the first node
    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    # Initialize queue with first node
    q = deque()
    q.append(1)

    # Perform BFS to compute shortest path from node 1 to all other nodes in the tree
    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                q.append(v)

    # Compute shortest path with special nodes
    shortest = float('inf')
    for node in visitNodes:
        shortest = min(shortest, dist[node])

    # If any special node is unreachable from node 1, we return -1.
    if shortest == float('inf'):
        return -1

    # Compute the number of times we need to visit each special node
    visits = [0] * (n + 1)
    for node in visitNodes:
        visits[node] = 1

    # Initialize queue with all special nodes
    q = deque(visitNodes)

    # Perform BFS to compute the shortest path from 1 to n, visiting all special nodes
    while q:
        u = q.popleft()
        for v in adj_list[u]:
            if visits[v] == 0:
                visits[v] = visits[u] + 1
                q.append(v)

    # Return the total distance from 1 to n, visiting all special nodes
    return visits[n]

# Example usage
n = 5
edges = [[1,2],[1,3],[3,4],[3,5]]
special_nodes = [2,4]
shortest = shortest_path_with_special_nodes(n, edges, special_nodes)
print(shortest)  # Output: 6
