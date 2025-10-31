# https://www.hellointerview.com/learn/code/depth-first-search/global-variables

from fundamentals import Node

# Given the root node of a binary tree, write a function to find the number of "good nodes" in the tree.
# A node X in the tree is considered "good" if in the path from the root to the node X, there are no nodes with a value greater than X's value.

#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

# Helper Function
# Use when: You only need to count good nodes, not access them.
#  - Most efficient for counting
#  - Clean, simple logic
#  - Returns an integer

def goodNodes(root: Node):
    def dfs(root: Node, max_):
        if root is None:
            return 0

        count = 0
        if root.val >= max_:
            count += 1
            max_ = root.val

        left = dfs(root.left, max_)
        right = dfs(root.right, max_)

        return left + right + count

    return dfs(root, float('-inf'))


# Global Variables
#  Use when: You need to collect the actual nodes.
#  - Uses nonlocal to modify outer scope variable
#  - Good for building up a result list
#  - Caution: Can be harder to debug and test since it has side effects

def goodNodes(root):
    nodes = []

    def dfs(root, max_):
        nonlocal nodes
        if root is None:
            return

        if root.val >= max_:
            max_ = root.val
            nodes.append(root)

        dfs(root.left, max_)
        dfs(root.right, max_)

    dfs(root, -float('inf'))
    return nodes

# Alt Approach 1
#  Use when: You want a pure functional approach (no side effects).
#  - Returns new lists, combines them
#  - Easier to reason about and test
#  - Downside: Less efficient - creates many intermediate lists

def goodNodes(root):
    def dfs(root, max_):
        if root is None:
            return []

        result = []
        if root.val >= max_:
            max_ = root.val
            result.append(root)

        left = dfs(root.left, max_)
        right = dfs(root.right, max_)
        return result + left + right
    return dfs(root, float('-inf'))

# Alt Approach 2
#Use when: You want to thread state through recursive calls.
#  - Passes the accumulator as a parameter
#  - Note: This approach has a bug - it doesn't explore both subtrees correctly since nodes gets mutated
#  and passed through left before right
#  - Generally avoid this pattern unless you need specific left-to-right processing

def goodNodes(root):
    def dfs(root, max_, nodes):
        if root is None:
            return nodes

        if root.val >= max_:
            max_ = root.val
            nodes.append(root)

            left = dfs(root.left, max_, nodes)
            # need to pass the result from the
            # left to the right subtree
            right = dfs(root.right, max_, left)

            return right

    return dfs(root, float('-inf'))
