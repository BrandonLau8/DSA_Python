# https://www.hellointerview.com/learn/code/depth-first-search/copy-graph

class Node:
    def __init__(self, value=0, neighbors=None):
        self.value = value
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = [] 

def clone_graph(node):
    adj_list = {}
    
    def dfs(node):
        if node.value in adj_list:
            return
        
        #Put values in adj_list
        values = []
        for n in node.neighbors:
            values.append(n.value)
        adj_list[node.value] = values
        
        #Go to next node
        for n in node.neighbors:
            dfs(n)
        
    if node:
        dfs(node)
        
    return adj_list