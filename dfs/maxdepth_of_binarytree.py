# https://www.hellointerview.com/learn/code/depth-first-search/maximum-depth-of-binary-tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root:Node) -> int:
    if root is None:
        return 0
    
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return max(left, right) + 1
    