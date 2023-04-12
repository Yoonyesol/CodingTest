import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    tower[x] = 0
    while queue:
        x = queue.popleft()
        if x == g:
            return tower[x]
        for nx in [x+u, x-d]:
            if nx > f or nx <= 0:
                continue
            if tower[nx] == -1:
                tower[nx] = tower[x] + 1
                queue.append(nx)
    return "use the stairs"

f, s, g, u, d = map(int, sys.stdin.readline().split())
tower = [-1] * (f+1)
print(bfs(s))