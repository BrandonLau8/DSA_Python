import heapq

times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7

def greedy_min_make_span(T, m):
    n = len(T)
    A = [None] * n  # Job assignments, initially None
    M = [0] * m     # Processor loads, initially 0

    # Min-heap of (current_load, processor_id)
    heap = [(0, j) for j in range(m)]
    heapq.heapify(heap)

    for i in range(n):
        load, j = heapq.heappop(heap)   # Processor with least load
        print(load, j)
        A[i] = j                        # Assign job i to processor j
        load += T[i]                    # Update the load
        heapq.heappush(heap, (load, j)) # Put processor back in heap with updated load

    return print(A)

greedy_min_make_span(times, m)

m = 