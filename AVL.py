class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        
    def get_height(self, node):
        if not node:
            return 0
        return node.height
        
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    def right_rotate(self, y: "Node"):
        x = y.left
        pivot_subtree = x.right
        
        x.right = y
        y.left = pivot_subtree
        
        self.update_height(y)
        self.update_height(x)
        
        return x # New root
        
    def left_rotate(self, x: "Node"):
        y = x.right
        pivot_subtree = y.left
        
        y.left = x
        x.right = pivot_subtree
        
        self.update_height(x)
        self.update_height(y)
        
        return y #New root
    
    def insert(self, node, key):
        #Normal BST insertion
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
            
        self.update_height(node)
        
        balance = self.get_balance(node)
        
        #4 cases of Imbalance
        
        # Left-Left
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)
        
        # Right - Right
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)
        
        # Left - Right
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right - Left
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)
        
    
tree = Node(0)
root = None
values = [10, 20, 30, 40, 50, 25]

for v in values:
    root = tree.insert(root, v)
    
tree.inorder(root)
print('\n')