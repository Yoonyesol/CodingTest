import sys
from collections import deque
i = int(sys.stdin.readline())
queue = deque(i+1 for i in range(i))
while queue:
    if len(queue) == 1:
        print(queue.popleft())
        break
    queue.popleft()
    queue.append(queue.popleft())