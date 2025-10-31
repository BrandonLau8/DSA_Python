coins = [5, 20, 25]
target = 40

def dp(target, coins):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')

    T = [float('inf')] * (target+1)
    S = [-1] * (target+1)
    
    T[0] = 0
        
    for c in range(1, target+1):
        for coin in coins:
            if c - coin >= 0 and T[c -coin] != float('inf'):
                if T[c-coin] + 1 < T[c]:
                    T[c] = T[c-coin] +1
                    S[c] = coin
    # print(T)        
    # print(S)
    
    used = []
    x = target
    while x>0:
        used.append(S[x])
        x -= S[x]
    
    print("Minimum number of coins:", T[target])
    print("Coins used:", used)
    
    
    
dp(target, coins)