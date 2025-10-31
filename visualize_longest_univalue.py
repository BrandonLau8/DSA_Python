"""
Visual animation of the Longest Univalue Path algorithm
Shows step-by-step DFS traversal and path computation
"""

import time
import os

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def print_tree(root, highlight=None, prefix="", is_tail=True):
    """Print tree structure with highlighting"""
    if not root:
        return

    # Color codes
    RESET = '\033[0m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'

    connector = "└── " if is_tail else "├── "

    # Highlight current node
    if root == highlight:
        print(f"{prefix}{connector}{YELLOW}{BOLD}[{root.val}] ← CURRENT{RESET}")
    else:
        print(f"{prefix}{connector}{GREEN}{root.val}{RESET}")

    extension = "    " if is_tail else "│   "

    if root.left or root.right:
        if root.right:
            print_tree(root.right, highlight, prefix + extension, False)
        if root.left:
            print_tree(root.left, highlight, prefix + extension, True)

def longestunivaluepath_animated(root):
    """Animated version showing each step"""
    max_length = 0
    step = [0]  # Use list to allow modification in nested function

    def dfs(node):
        nonlocal max_length

        step[0] += 1
        current_step = step[0]

        # Show entering node
        clear_screen()
        print("=" * 60)
        print(f"STEP {current_step}: Entering DFS on node {node.val if node else 'None'}")
        print("=" * 60)
        print_tree(root, highlight=node)
        print()

        if not node:
            print("→ Node is None, returning 0")
            time.sleep(1.5)
            return 0

        print(f"→ Processing node with value: {node.val}")
        time.sleep(1.5)

        # Recurse left
        print(f"\n→ Going LEFT from node {node.val}...")
        time.sleep(1)
        left_length = dfs(node.left)

        # Show return from left
        clear_screen()
        print("=" * 60)
        print(f"STEP {step[0]}: Returned from LEFT of node {node.val}")
        print("=" * 60)
        print_tree(root, highlight=node)
        print()
        print(f"→ left_length = {left_length}")
        time.sleep(1.5)

        # Recurse right
        print(f"\n→ Going RIGHT from node {node.val}...")
        time.sleep(1)
        right_length = dfs(node.right)

        # Show return from right
        clear_screen()
        print("=" * 60)
        print(f"STEP {step[0]}: Returned from RIGHT of node {node.val}")
        print("=" * 60)
        print_tree(root, highlight=node)
        print()
        print(f"→ left_length = {left_length}")
        print(f"→ right_length = {right_length}")
        time.sleep(1.5)

        # Calculate arrows
        left_arrow = right_arrow = 0

        print(f"\n→ Checking if we can extend paths through node {node.val}...")

        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
            print(f"  ✓ LEFT child ({node.left.val}) == current ({node.val})")
            print(f"    left_arrow = {left_length} + 1 = {left_arrow}")
        else:
            print(f"  ✗ LEFT child doesn't match or is None")

        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1
            print(f"  ✓ RIGHT child ({node.right.val}) == current ({node.val})")
            print(f"    right_arrow = {right_length} + 1 = {right_arrow}")
        else:
            print(f"  ✗ RIGHT child doesn't match or is None")

        time.sleep(2)

        # Update max_length
        path_through_node = left_arrow + right_arrow
        print(f"\n→ Path through this node: {left_arrow} + {right_arrow} = {path_through_node}")

        old_max = max_length
        max_length = max(max_length, path_through_node)

        if max_length > old_max:
            print(f"  🎉 NEW MAX LENGTH: {old_max} → {max_length}")
        else:
            print(f"  max_length stays: {max_length}")

        time.sleep(2)

        # Return value
        return_value = max(left_arrow, right_arrow)
        print(f"\n→ Returning: max({left_arrow}, {right_arrow}) = {return_value}")
        print(f"  (This is the longest univalue path going UP from node {node.val})")
        time.sleep(2)

        return return_value

    dfs(root)

    # Final result
    clear_screen()
    print("=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print_tree(root)
    print()
    print(f"🏆 Longest Univalue Path Length: {max_length}")
    print("=" * 60)

    return max_length

# Example 1: Tree with same values
print("Creating example tree:")
print("""
        5
       / \\
      4   5
     / \\   \\
    1   1   5

Expected longest univalue path: 2 (right side: 5-5-5)
""")

root1 = TreeNode(5)
root1.left = TreeNode(4)
root1.right = TreeNode(5)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(1)
root1.right.right = TreeNode(5)

input("\nPress Enter to start animation...")
result = longestunivaluepath_animated(root1)

print("\n" + "=" * 60)
print("\nTry another example? (Example 2: All same values)")
print("""
        1
       / \\
      1   1
     / \\
    1   1

Expected longest univalue path: 4 (going through root)
""")

if input("\nRun example 2? (y/n): ").lower() == 'y':
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(1)

    result2 = longestunivaluepath_animated(root2)
