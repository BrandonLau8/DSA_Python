# https://www.hellointerview.com/learn/code/depth-first-search/path-sum-2

from fundamentals import Node

def pathsum(root:Node, target:int) -> int:
    def dfs(node:Node, target:int, path:list[int]):
        if not node:
            return
        
        path.append(node.val)
        if not node.left and not node.right:
            if node.val == target:
                res.append(path[:]) #appends the copy of path at current state
                
        dfs(node.left, target - node.val, path)
        dfs(node.right, target - node.val, path)
        path.pop()
        
    res = []
    dfs(root, target, [])
    return res