# https://www.hellointerview.com/learn/code/depth-first-search/adjacency-list

def build_adj_list(n, edges):
    adj_list = {}
    
    for i in range(n):
        adj_list[i] = []
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
        return adj_list
    
def dfs(adjList):
    if not adjList:
        return
    visited = set()
    
    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        for neighbor in adjList[node]:
            dfs_helper(neighbor)
        return
    
    for node in adjList:
        if node not in visited:
            dfs_helper(node)