# https://www.hellointerview.com/learn/code/depth-first-search/fundamentals

class Node:
    def __init__(self, val:int):
        self.val:int = val
        self.left:Node = None
        self.right:Node = None
        

def dfs(root:Node):
    if root is None:
        return
    
    dfs(root.left)
    dfs(root.right)
    return

def maxValue(node:Node) -> int:
    if node is None:
        return float('-inf')
    
    left = maxValue(node.left)
    right = maxValue(node.right)
    
    return sum(left.val, right.val, node.val)

