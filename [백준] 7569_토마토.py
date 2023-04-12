import sys
from collections import deque

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= m or ny >= n or nz >= h or nx < 0 or ny < 0 or nz < 0:
                continue
            if mato[nz][ny][nx] == 0:
                mato[nz][ny][nx] = mato[z][y][x] + 1
                queue.append((nx, ny, nz))

m, n, h = map(int, sys.stdin.readline().split())
mato = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        mato[i].append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if mato[i][j][k] == 1:
                queue.append((k, j, i))
bfs()

flag = False
answer = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if mato[i][j][k] == 0:
                flag = True
                break
            answer = max(answer, mato[i][j][k])
if flag:  #토마토가 모두 익지 못하는 상태
    answer = -1
else:
    answer -= 1
print(answer)