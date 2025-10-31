class Graph:
    def __init__(self):
        self.adj_list:dict = {} #Key = Node:any, Value = Neighbors:list 
        
    def add_node(self, node):
        if node not in self.adj_list: #Ensure there are no duplicates
            self.adj_list[node] = [] 
            
    def add_edge(self, node1, node2):
        #For undirected graph
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def get_nodes(self):
        return list(self.adj_list.keys())
    
    def get_neighbors(self, node):
        return self.adj_list.get(node, []) #If node is not in graph, return []
    
    
    def update_node(self, old_node, new_node):
        # Check if the node exists
        if old_node not in self.adj_list:
            return

        # Step 1: Copy the neighbors from old_node to new_node
        neighbors = self.adj_list[old_node]
        self.adj_list[new_node] = neighbors

        # Step 2: Remove old_node from the graph
        del self.adj_list[old_node]

        # Step 3: Go through each node in the graph
        for node in self.adj_list:
            new_neighbors = []
            for neighbor in self.adj_list[node]:
                # If the neighbor is the old_node, replace it with new_node
                if neighbor == old_node:
                    new_neighbors.append(new_node)
                else:
                    new_neighbors.append(neighbor)
            # Update the neighbor list
            self.adj_list[node] = new_neighbors
        def remove_edge(self, node1, node2):
            if node1 in self.adj_list and node2 in self.adj_list[node1]:
                self.adj_list[node1].remove(node2)
            if node2 in self.adj_list and node1 in self.adj_list[node2]:
                self.adj_list[node2].remove(node1)
            
    def remove_node(self, node):
        if node in self.adj_list:
                # Remove node in all neighbors
            for neighbor in self.adj_list[node]:
                self.adj_list[neighbor].remove(node)
            # Delete node
            del self.adj_list[node]
            
    
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_node('E')

# print("Nodes", g.get_nodes())
# print("Neighbors of B", g.get_neighbors('B'))

# g.update_node('D', 'X')
# print("After rename D to X", g.adj_list)

# g.remove_edge('A', 'C')
# print('After removing edge A-C', g.adj_list)

# g.remove_node('B')
# print('After removing node B:', g.adj_list)

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def create_node(self, node):
        if node not in self.adj_list:
           self.adj_list[node] = [] 
           
    def create_edge(self, node1, node2):
        self.create_node(node1)
        self.create_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def read_nodes(self):
        return self.adj_list.keys()
    
    def read_edges(self, node):
        return self.adj_list.get(node, [])