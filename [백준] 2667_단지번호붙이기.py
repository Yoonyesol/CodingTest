#DFS

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
house = []
danzi = []
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    if x >= n or y >= n or x < 0 or y < 0:
        return
    if house[x][y] == 1:
        cnt += 1
        house[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

answer = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            dfs(i, j)
            danzi.append(cnt)
            answer += 1
            cnt = 0
print(answer)
danzi.sort()
for i in danzi:
    print(i)


----------------
#BFS

import sys
from collections import deque

n = int(sys.stdin.readline())
house = []
danzi = []
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    house[x][y] = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if house[nx][ny] == 0:
                continue
            if house[nx][ny] == 1:
                house[nx][ny] = 0
                queue.append((nx, ny))

answer = 0
cnt = 0
for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            bfs(i, j)
            danzi.append(cnt)
            answer += 1
            cnt = 0
print(answer)
danzi.sort()
for i in danzi:
    print(i)