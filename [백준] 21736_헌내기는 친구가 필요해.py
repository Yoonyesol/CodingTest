#BFS: 14m 50s

import sys
from collections import deque

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    sch[x][y] = 'O'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if sch[nx][ny] == 'X':
                continue
            if sch[nx][ny] == 'P':
                cnt += 1
                sch[nx][ny] = 'X'
                queue.append((nx, ny))
            if sch[nx][ny] == 'O':
                sch[nx][ny] = 'X'
                queue.append((nx, ny))
        
n, m = map(int, sys.stdin.readline().split())
sch = []
for _ in range(n):
    sch.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if sch[i][j] == "I":
            bfs(i, j)

if cnt == 0:
    print("TT")
else:
    print(cnt)


---------------
#DFS: 24m 35s

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    if x >= n or y >= m or x < 0 or y < 0:
        return
    if sch[x][y] == 'X':
        return
    if sch[x][y] == 'P':
        cnt += 1
    sch[x][y] = 'X'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)
        
n, m = map(int, sys.stdin.readline().split())
sch = []
for _ in range(n):
    sch.append(list(sys.stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if sch[i][j] == "I":
            dfs(i, j)

if cnt == 0:
    print("TT")
else:
    print(cnt)