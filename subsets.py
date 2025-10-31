def subsets_brute_force_iterative(nums):
    n = len(nums)
    result = []
    
    for i in range(2**n):
        subset = []
        
        for j in range(n):
            if i & (i << j):
                subset.append(nums[j])
                
        result.append(subset)
    
    return result