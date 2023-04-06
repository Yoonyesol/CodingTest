import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = []
for _ in range(N):
  miro.append(list(map(int, sys.stdin.readline().rstrip())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= N or ny >= M or nx < 0 or ny < 0:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
    return miro[N-1][M-1]

print(bfs(0, 0))