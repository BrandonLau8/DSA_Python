L = 100
sizes =  [ 1, 3, 5, 10, 30, 50, 75]
prices = [ 0.1, 0.2, 0.4, 0.9, 3.1, 5.1, 8.2]

# # Naive Attempt to Implement Recurrence
# def maxRevenue_Recursive(L:int, sizes:list, prices:list):
#     if L == 0:
#         return 0
#     if L < 0:
#         return float('-inf')
#     k = len(sizes)
#     assert len(prices) == k
    
#     optionValues = [prices[i] + maxRevenue_Recursive(L-sizes[i], sizes, prices) for i in range(k)]
#     optionValues.append(0) # Covers wasted material
#     bestValueSoFar = max(optionValues)
    
#     return bestValueSoFar
    
# # Adding Memoization
# def maxRevenue_Memoize(L, sizes, prices):
#     T = [0] * (L+1) # create an array of size L+1 and fill it with all 0s
#     k = len(sizes)
#     assert len(prices) == k
    
#     for l in range(1, L+1):
#         optionValues = []
#         for i in range(k):
#             if l-sizes[i] >= 0:
#                 optionValues.append(prices[i] + T[l-sizes[i]])
#         optionValues.append(0)
#         T[l] = max(optionValues)
#     return T[L]

# def maxRevenue_Memoize_with_Solution_Recovery(L, sizes, prices):
#     T = [0] * (L+1)
#     S = [-1] * (L+1)
    
#     k = len(sizes)
#     assert(len(prices) == k)
    
#     for l in range(1, L+1):
#         bestRevenue = 0
#         bestCutIndex = -1
#         for i in range(k):
#             cutSize = sizes[i]
#             if l - cutSize >= 0:
#                 currentRevenue = prices[i] + T[l-cutSize]
#                 if currentRevenue > bestRevenue:
#                     bestRevenue = currentRevenue
#                     bestCutIndex = i
        
#         T[l] = bestRevenue
#         S[l] = bestCutIndex
    
#     cuts = []
#     l = L
#     while l>0:
#         cutIndex = S[l]
#         if cutIndex == -1:
#             break
#         cutSize = sizes[cutIndex]
#         cuts.append(cutSize)
#         l -= cutSize
        
#     return T[L], cuts

# def maxRevenueMemoized(totalLength, cutSizes, cutPrices):
#     numCutTypes = len(cutSizes)
#     assert len(cutPrices) == numCutTypes

#     # Create DP table for max revenue at each length and cut index
#     maxRevenueTable = []  # DP table: maxRevenueTable[length][cutIndex]
#     decisionTable = []    # Records how many times to use each cut size

#     for length in range(totalLength + 1):
#         maxRevenueTable.append([0] * (numCutTypes + 1))
#         decisionTable.append([-1] * (numCutTypes + 1))

#     # Fill the DP table bottom-up
#     for length in range(totalLength + 1):
#         for cutIndex in range(numCutTypes - 1, -1, -1):  # From last cut to first
#             maxNumCuts = length // cutSizes[cutIndex]  # Max times current cut fits

#             # Try all cut counts from 0 up to maxNumCuts
#             possibleOptions = []
#             for count in range(maxNumCuts + 1):
#                 cutLength = count * cutSizes[cutIndex]
#                 cutRevenue = count * cutPrices[cutIndex]
#                 remainingLength = length - cutLength
#                 futureRevenue = maxRevenueTable[remainingLength][cutIndex + 1]
#                 totalRevenue = cutRevenue + futureRevenue
#                 possibleOptions.append((totalRevenue, count))

#             # Also consider the "waste" option (skip this size)
#             possibleOptions.append((0, -1))

#             # Pick best option
#             bestRevenue, bestCount = max(possibleOptions)
#             maxRevenueTable[length][cutIndex] = bestRevenue
#             decisionTable[length][cutIndex] = bestCount

#     # Reconstruct the cut combination from decision table
#     cutsUsed = []
#     remainingLength = totalLength
#     cutIndex = 0

#     while remainingLength > 0 and cutIndex < numCutTypes:
#         chosenCount = decisionTable[remainingLength][cutIndex]

#         if chosenCount == -1:
#             break  # waste case, no valid cut

#         if chosenCount > 0:
#             cutsUsed.append(f"Cut length = {cutSizes[cutIndex]}, {chosenCount} times")

#         # Reduce rod length by amount cut
#         remainingLength -= chosenCount * cutSizes[cutIndex]
#         cutIndex += 1

#     return maxRevenueTable[totalLength][0], cutsUsed
    
    
# def maxRevenue(L, cutSizes, prices):
#     # Base Cases
#     if L == 0:
#         return 0
#     if L < 0:
#         return float('-inf')
    
#     maxRev = float('-inf')
    
#     for l in range(len(cutSizes)):
#         cut = cutSizes[l]
#         price = prices[l]
#         rev = maxRevenue((L - cut), cutSizes, prices)
#         if rev != float('inf'):
#             maxRev = max(maxRev, rev+price)
            
#     return maxRev

L = 10
sizes = [3, 4]
prices = [1.8, 2]

def maxRevenue_memo(L, sizes, prices):
    # Base Cases
    if L == 0:
        return 0
    if L < 0:
        return float('-inf')
    
    # Add Memo and Solution Table
    T = [float('-inf')] * (L+1)
    S = [-1] * (L+1)
    
    T[0] = 0
    
    # Calculate Revenue using cutSize
    for l in range(1, L+1):
        
        for i in range(len(sizes)):
            
            cut = sizes[i]
            price = prices[i]
            
            if l - cut >= 0 and T[l-cut] != float('-inf'):
                rev = T[l-cut] + price

                if rev > T[l]:
                # Put the max at cutSize into Memo
                    T[l] = rev

                # Put the cutSize into Solution
                    S[l] = cut
    # With the L, Calculate cutSize by scanning Solution Table 
    print(T)
    print(S)
    
    cuts = []
    cut_L = L
    while cut_L > 0 and S[cut_L] != -1:
        cuts.append(S[cut_L])
        cut_L -= S[cut_L]  
    
    print('Cuts', cuts)
    print('Max Revenue', T[L])
    
maxRevenue_memo(L, sizes, prices)