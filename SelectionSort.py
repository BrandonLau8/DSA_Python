arr = [4, 2, 9, 1, 7, 6]

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i #Start by assuming the current i is the min
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]: #Find a smaller element
#                 min_index = j
#         #Swap the smallest found with the first unsorted element
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#     return print(arr)
    
# selection_sort(arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return print(arr)


selection_sort(arr)