class Graph:
    def __init__(self):
        self.adj_list:dict = {}
    
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []
            
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
        
    def get_nodes(self):
        return list(self.adj_list.keys())
    
    def get_neighbors(self, node):
        return self.adj_list.get(node, [])
    
    def update_node(self, old_node, new_node):
        if old_node not in self.adj_list:
            return
        for node in self.adj_list:
            new_neighbors = []
            for neighbor in self.adj_list[node]:
                if neighbor == old_node:
                    new_neighbors.append(new_node)
                else:
                    new_neighbors.append(neighbor)
            self.adj_list[node] = new_neighbors
            
    def remove_edge(self, node):
        if node in self.adj_list:
            for neighbor in self.adj_list[node]:
                self.adj_list[neighbor].remove(node)
            del self.adj_list[node]

    def has_path(self, start, end):
        if start not in self.adj_list or end not in self.adj_list:
            return False
        if start == end:
            return True

        visited = set()
        stack = [start]

        while stack:
            current = stack.pop()
            if current == end:
                return True
            if current in visited:
                continue
            visited.add(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return False