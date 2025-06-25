class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insert(root, value):
    if root is None:
        return Node(value)
    
    queue = [root]
    while queue:
        current = queue.pop(0)
        if not current.left:
            current.left = Node(value)
            return root
        else:
            queue.append(current.left)
            
        if not current.right:
            current.right = Node(value)
            return root
        else:
            queue.append(current.right)
            

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)
        