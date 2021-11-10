from collections import deque

queue = deque([])

queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

queue.popleft()
queue.pop()
queue.pop()

print(queue)

if not queue:
    print("empty")
else: 
    print(queue[-1])