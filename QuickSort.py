def quick_sort(arr, low, high):
    #Base case
    if low < high:
        #Partition the array
        pivot_index = partition(arr, low, high)
        
        #Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
        
        
    return arr
    
def partition(arr, low, high):
    pivot = arr[high] #Choose the last element as pivot
    i = low - 1 #Pointer for the smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            #Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot after the last smaller element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the pivot index
    return i+1

arr = [4, 2, 9, 1 ,7, 6]

print(quick_sort(arr, 0, 5))

