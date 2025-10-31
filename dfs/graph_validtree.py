# https://www.hellointerview.com/learn/code/depth-first-search/graph-valid-tree

from typing import List


#   For n=5, edges=[[0,1], [0,2], [0,3], [1,4]]:
#       0
#      /|\
#     1 2 3
#    /
#   4
#   ✅ Valid tree (no cycles, all connected)

#   For n=5, edges=[[0,1], [1,2], [2,3], [1,3], [1,4]]:
#       0
#       |
#       1---4
#      / \
#     2---3  (cycle: 1→2→3→1)
#   ❌ Invalid (has cycle)


def validTree(n:int, edges:List[List[int]]):
    adj_list = []
    for _ in range(n):
        adj_list.append([])
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Use DFS to check if the graph is a valid tree
    visited = [False] * n
    if hasCycle(adj_list, 0, visited, -1):
        return False
    
    for node_visited in visited:
        if node_visited == False:
            return False
    return True

def hasCycle(adj_list, node, visited, parent):
    visited[node] = True
    for neighbor in adj_list[node]:
        if visited[neighbor] and parent != neighbor:
            return True
        elif not visited[neighbor] and hasCycle(adj_list, neighbor, visited, node):
            return True
    return False