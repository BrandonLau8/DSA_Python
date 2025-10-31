from collections import deque


queue = deque()
queue = deque(["A", "B", "C"])

print(queue[0])
print(queue[-1])
print(list(queue))

queue[0] = 'B'

queue.popleft()
queue.clear()

queue.append('B')
queue.appendleft('Z')