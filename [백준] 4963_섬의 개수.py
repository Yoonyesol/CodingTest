import sys
from collections import deque

dy = [-1, 1, 0, 0, -1, 1, -1, 1]
dx = [0, 0, -1, 1, 1, 1, -1, -1]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= h or ny >= w or nx < 0 or ny < 0:
                continue
            if island[nx][ny] == 0:
                continue
            if island[nx][ny] == 1:
                island[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    island = []
    for i in range(h):
        island.append(list(map(int, sys.stdin.readline().split())))
    visited = [[0] * w for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)