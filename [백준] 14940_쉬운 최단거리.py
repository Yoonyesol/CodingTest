import sys
from collections import deque
input=sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny] != -1:
                continue
            if arr[nx][ny] == 0:    #방문할 수 없는 땅
                visited[nx][ny] = 0 #방문x 표시
                continue
            if arr[nx][ny] == 1:    #방문할 수 있는 땅
                visited[nx][ny] = visited[x][y] + 1 #이전 땅까지의 거리+1
                q.append((nx,ny))   #다음에 방문할 땅 추가

for x in range(n):
    for y in range(m):
        if arr[x][y] == 2 and visited[x][y] == -1:  #방문하지 않은 목표지점에서 출발
            bfs(x,y)    #bfs로 갈 수 있는 모든 땅 순회하며 거리 측정

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:  #갈 수 없는 땅은 0 출력
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()