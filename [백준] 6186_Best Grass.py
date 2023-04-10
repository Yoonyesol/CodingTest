import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
grass = []
for _ in range(r):
    grass.append(list(sys.stdin.readline().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    grass[x][y] = "0"
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= r or ny >= c or nx < 0 or ny < 0:
                continue
            if grass[nx][ny] == ".":
                continue
            if grass[nx][ny] == "#":
                grass[nx][ny] = "0"
                queue.append((nx, ny))
answer = 0
for i in range(r):
    for j in range(c):
        if grass[i][j] == "#":
            bfs(i, j)
            answer += 1
print(answer)