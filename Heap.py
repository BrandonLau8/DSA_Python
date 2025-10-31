import heapq

heap = []
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -7)

print([-x for x in heap])
print(type(heap))