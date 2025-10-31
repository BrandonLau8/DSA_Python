# https://www.hellointerview.com/learn/code/depth-first-search/diameter-of-a-binary-tree

from fundamentals import Node

def diameter(root: Node) -> int:
   max_=0
   def dfs(node):
       nonlocal max_
       if not node:
           return 0
       
       left=dfs(node.left)
       right=dfs(node.right)
       
       max_=max(max_, left+right)
       
       return max(left,right) +1
   dfs(root)
   return max_

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    import pdb
    pdb.set_trace()
    result = diameter(root)
    print(result)