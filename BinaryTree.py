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
        
def update_node(root, old_value, new_value):
    if root is None:
        return False
    
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.value == old_value:
            current.value = new_value
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

def delete_node(root, value):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.value == value:
            return None
        else:
            return root
        
    queue = [root]
    node_to_delete = None
    last_node = None
    
    while queue:
        last_node = queue.pop(0)
        if last_node.value == value:
            node_to_delete = last_node
        if last_node.left:
            queue.append(last_node.left)
        if last_node.right:
            queue.append(last_node.right)
    
    if node_to_delete:
        node_to_delete = last_node.value
        delete_deepest(root, last_node)
        
    return root

def delete_deepest(root, d_node):
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current is d_node:
            current = None
            return
        if current.right:
            if current.right is d_node:
                current.right = None
                return
            queue.append(current.right)
        if current.left:
            if current.left is d_node:
                current.left = None
                return
            queue.append(current.left)
    