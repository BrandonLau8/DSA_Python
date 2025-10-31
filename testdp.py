import heapq

def min_cost_to_combine_rods(lengths):
    heapq.heapify(lengths)
    total_cost = 0

    while len(lengths) > 1:
        # Pop the two smallest lengths
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        cost = first + second
        total_cost += cost

        # Push the combined rod back into the heap
        heapq.heappush(lengths, cost)
        print(lengths)

    return total_cost

# Example
rods = [1, 5, 2, 4, 3, 2]
print("Minimum cost:", min_cost_to_combine_rods(rods))  # Output: 33

def min_partition_difference(nums):
    total = sum(nums)
    target = total // 2
    n = len(nums)

    # dp[i] = True if a subset with sum i is possible
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # Find the closest possible sum to total//2
    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2 * i  # min difference

# Example
nums = [1, 2, 3, 9]
print("Minimum difference:", min_partition_difference(nums))  # Output: 3

def computeBestPartition(l):
    n = len(l)
    assert n >= 1
    assert all(elt >= 1 and elt == int(elt) for elt in l)

    total = sum(l)
    target = total // 2

    # dp[i] = set of indices that sum to i
    dp = [None] * (target + 1)
    dp[0] = set()

    for idx, num in enumerate(l):
        for j in range(target, num - 1, -1):
            if dp[j - num] is not None and dp[j] is None:
                dp[j] = dp[j - num] | {idx}

    # Find best possible sum ≤ total // 2
    for i in range(target, -1, -1):
        if dp[i] is not None:
            indices = dp[i]
            l1 = [l[idx] for idx in indices]
            l2 = [l[idx] for idx in range(n) if idx not in indices]
            return l1, l2
        
def longest_path(rootNode):
    max_depth = [0]
    
    def dfs(node):
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        max_depth[0] = max(max_depth[0], left + right + 1)
        
        return max(left, right) + 1
    
    dfs(rootNode)
    
    return max_depth[0]
        