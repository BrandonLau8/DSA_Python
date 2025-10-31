class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
def cloneGraph(node: Node | None) -> Node | None:
    visited = {}
    def dfs(node):
        if node in visited:
            return visited[node]
        
        copy = Node(node.val)
        visited[node] = copy
        
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    
    return dfs(node) if node else None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

#BFS
from collections import deque

def print_all_nodes(node: Node):
    visited = set()
    queue = deque([node])
    
    while queue:
        node = queue.popleft()
        if node.val not in visited:
            print(f'Node {node.val}, neighbors:', [n.val for n in node.neighbors])
            visited.add(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    
# print_all_nodes(cloneGraph(n1))

#DFS
def print_all_nodes_dfs(node, visited=None):
    if visited is None:
        visited = set()
        
    if node.val in visited:
        return
    
    print(f'Node {node.val}, neighbors:', [n.val for n in node.neighbors])
    visited.add(node.val)
    
    for neighbor in node.neighbors:
        print_all_nodes_dfs(neighbor, visited)
        
print_all_nodes_dfs(cloneGraph(n1))