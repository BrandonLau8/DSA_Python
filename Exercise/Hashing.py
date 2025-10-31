
arr = [1, 2, 2, 3, 3, 3, 4, 1, 2]
# Count occurrences of elements in an array.
def count_occurences(arr):
    freq = {}
    for num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
    return freq

# Find the first non-repeating character in a string.
def first_non_repeating_char(s):
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None  

# Subarray with given sum.
def subarray_sum(arr, target):
    n = len(arr)
    curr_sum = 0
    left = 0
    
    for right in range(n):
        curr_sum += arr[right]
        
        while curr_sum > target and left <= right:
            curr_sum -= arr[left]
            left+=1
        if curr_sum == target:
            return (left, right)
    return None

# Two sum using hash map.
def twosum(arr, target):
    seen={}
    for i, num in enumerate(arr):
        compl = target - num
        if compl in seen:
            return (i, seen[compl])
        else:
            h[num] = i
    return None


# Group anagrams.
from collections import defaultdict
def group_anagrams(words):
    anagrams = {} 
    
    for word in words:
       key = ''.join(sorted(word))
       
       if key in anagrams:
           anagrams[key].append(word)
           
       else:
           anagrams[key] = [word]
    result = []
    for group in anagrams.values():
        result.append(group)
    return result