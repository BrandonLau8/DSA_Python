from collections import deque

def bfs(graph:dict, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node)
            visited.add(node)
            
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