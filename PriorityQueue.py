import heapq



def minpriority():
    pq = []
    heapq.heappush(pq, (1, 'Task A'))
    heapq.heappush(pq, (3, 'Task B'))
    heapq.heappush(pq, (2, 'Task C'))

    print(pq)

    while(pq):
        priority, task = heapq.heappop(pq)
        print(f'Processing {task} with priority {priority}')
        
    print(pq)

def maxpriority():
    pq = []
    heapq.heappush(pq, (-5, 'Task C'))
    heapq.heappush(pq, (-10, 'Task A'))
    heapq.heappush(pq, (-7, 'Task B'))
    
    print(pq)
    
    while(pq):
        priority, task = heapq.heappop(pq)
        print(f'Processing {task} with priority {-priority}')

minpriority()
maxpriority()