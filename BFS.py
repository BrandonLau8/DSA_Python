from collections import deque

def bfs(graph, start):
    visited = set()                 # To track visited nodes
    queue = deque([start])          # Use a queue for BFS

    while queue:
        node = queue.popleft()      # Remove from front of queue

        if node not in visited:
            print(node)             # Visit the node
            visited.add(node)       # Mark as visited

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

