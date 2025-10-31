arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
answer = 6

#Brute Force
def bruteforce(arr):
    n = len(arr)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return print(max_sum)

#MergeSort
def mergesort(arr, left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    
    left_max = mergesort(arr, left, mid)
    right_max = mergesort(arr, mid+1, right)
    cross_max = crossing_sum(arr, left, mid, right)
    
    return max(left_max, right_max, cross_max)
    
def helper(arr):
    return mergesort(arr, 0, len(arr)-1)
    
def crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    total = 0
    
    for i in range(mid, left -1, -1):
        total+=arr[i]
        left_sum = max(left_sum, total)
        
    right_sum = float('-inf')
    total = 0
    
    for i in range(mid+1, right+1):
        total += arr[i]
        right_sum = max(right_sum, total)
        
    return left_sum + right_sum

print(helper(arr))

#Kadanes Algorithm
