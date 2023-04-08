import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    baechu[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            if baechu[nx][ny] == 1:
                baechu[nx][ny] = 0
                queue.append((nx, ny))

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    baechu = [[0 for _ in range(n)] for _ in range(m)]
    
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        baechu[a][b] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if baechu[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)