arr = [4, 2, 9, 1, 7, 6]
str = 'hello'

# Reverse an array or string.
print(str[:])
print(arr[::-1])
print(str[::-1])


# Find the maximum and minimum element in an array.
print(max(arr))
print(min(arr))

# Rotate an array by k positions.
def rotate(arr, k):
    n=len(arr)
    k=k%n #handle k> n
    return arr[-k:]+arr[:-k]
print(rotate(arr, 3))

# Two sum problem (finding a pair with a given sum).
def twosum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            twosum = arr[i] + arr[j]
            if twosum == target:
                return (i, j)
    return None

# Check if a string is a palindrome.
def checkpal(str):
    str = str.lower()
    
    filtered=""
    for char in str:
        if char.isalnum():
            filtered+=char

    left, right = 0, len(str)-1
    while left<right:
        if str[left] != str[right]:
            return False
        left+=1
        right-=1
    return True
print(checkpal(str))


# Count frequencies of elements.
def count_freq(arr):
    freq=dict()
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        freq[arr[i]] = count
    return freq

# Sort ascending
arr.sort()

# Sort descending
arr.sort(reverse=True)

# Sort letters alphabetically
sorted_str = ''.join(sorted(str))
sorted_str_rev = ''.join(sorted(str, reverse=True))

# CRUD
nums = [1, 2, 3, 4]

nums.append(4)
nums.insert(1, 10)
nums.extend([5, 6])

nums[0]
nums[-1]
nums[1:4]

nums[2] = 20

# By Index
del nums[3]
nums.pop(0)

# By Value
nums.remove(0)

# By slice
nums[1, 3] = []
