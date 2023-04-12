import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
sumba = [0 for _ in range(100001)]

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        if x == k:
            return sumba[x]
        for nx in (x-1, x+1, 2*x):
            if nx < 0 or nx >= 100001:
                continue
            if sumba[nx] == 0:
                sumba[nx] = sumba[x] + 1
                queue.append(nx)        
print(bfs(n))
