import sys
from collections import deque

n = int(sys.stdin.readline())
game = []
for _ in range(n):
    game.append(list(map(int, sys.stdin.readline().split())))
visited = [[0] * n for _ in range(n)]

dy = [0, 1]
dx = [1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx = x + dx[i] * game[x][y]
            ny = y + dy[i] * game[x][y]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] == 1:
                continue
            if game[nx][ny] == 0:
                continue
            if game[nx][ny] == -1:
                return "HaruHaru"
            queue.append((nx, ny))
            visited[nx][ny] = 1
    return "Hing"

print(bfs(0, 0))