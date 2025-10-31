nums = [1, 2, 3, 4]

def nestedloops(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print((nums[i], nums[j]))
            
# nestedloops(nums)

def combine(nums, k):
    res = []
    
    def backtrack(start, path):
        if len(path) == k:
            res.append(path.copy())
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return print(res)

combine(nums, 2)
