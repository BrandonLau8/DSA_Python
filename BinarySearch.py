arr = [1, 3, 5, 7, 9, 11, 13, 15, 16]

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + (right - left)) // 2
        
#         print(f'Left:{left}, Right: {right}, Mid: {mid}, arr[mid]: {arr[mid]}')
#         if arr[mid] == target:
#             print(f'Found {target} at index {mid}')
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#             print(f'{arr[mid]} < {target}, move right')
#         else:
#             right = mid - 1
#             print(f'{arr[mid] > target}, move left')
            
#     return -1

def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    res = -1
    step = 1
    
    while low <= high:
        mid = low + (high - low) // 2
        print(f"Step {step}: low={low}, mid={mid}, high={high}, nums[mid]={nums[mid]}")
        
        if nums[mid] >= target:
            res = mid
            print(f"  nums[mid] >= target ({nums[mid]} >= {target}) → res={res}, move high to {mid-1}")
            high = mid - 1
        else:
            print(f"  nums[mid] < target ({nums[mid]} < {target}) → move low to {mid+1}")
            low = mid + 1
        step += 1
        
    print(f"Final result index: {res}")
    return res

binary_search(arr, 13)