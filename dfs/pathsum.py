# https://www.hellointerview.com/learn/code/depth-first-search/path-sum

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def pathSum(root:Node, target:int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        return target == root.val
    
    
    left = pathSum(root.left, target - root.val)
    right = pathSum(root.right, target - root.val)
    
    return left or right #returns True if at least one is true