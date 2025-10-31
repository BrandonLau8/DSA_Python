n = [1,2, 3, 4, 5]

def fib_array(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        print(dp[i])
    return dp[n]

# fib_array(5)

def fib_hash(n, memo={}):
    
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n] = fib_hash(n-1, memo) + fib_hash(n-2, memo)
    print(memo[n])
    return memo[n]

fib_hash(5)