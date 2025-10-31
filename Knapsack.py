W = 5
items = [1, 2, 4]
prices = [2, 4, 6]

def knapsack(W, items, prices):
    n = len(items)
    T = [ [0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(W+1):
            
            item = i - 1
            itemWeight = items[item]
            value = prices[item]
            
            # if w == 0 or i == 0:
            #     return 0
            # if w < 0: 
            #     return float('-inf')
            
            if itemWeight <= w:
                T[i][w] = max(T[i-1][w], value + T[i-1][w-itemWeight])
            else:
                T[i][w] = T[i-1][w]
    
    print(T)
    
knapsack(W, items, prices)