# https://www.hellointerview.com/learn/code/depth-first-search/validate-binary-search-tree

# A tree is a BST if the following conditions are met:

# Every node on the left subtree has a value less than the value of the current node.
# Every node on the right subtree has a value greater than the value of the current node.
# The left and right subtrees must also be valid BSTs.


def validateBST(root) -> bool:
    def dfs(node, min_, max_) -> bool:
        if node is None:
            return True
        
        if node.val >= min_ or node.val >= max_:
            return False
    
        return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
    return dfs(root, float('-inf', float('inf')))