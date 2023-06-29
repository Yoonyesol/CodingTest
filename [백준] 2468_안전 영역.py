import sys
from collections import deque
input=sys.stdin.readline
n = int(input())
arr = []
arr_max = 0 #배열에서 가장 큰 숫자 저장하는 변수
for _ in range(n):
    a = list(map(int, input().split()))
    arr_max = max(max(a), arr_max)
    arr.append(a)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if arr[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
max_bfs = 0 #최대 ans(안전지대)값을 저장하는 변수
for k in range(arr_max+1):  #0~arr의 최대원소까지, 빗물의 양을 달리하며 안전지대의 갯수를 구함
    ans = 0 #안전지대 갯수 0으로 초기화
    visited = [[False] * n for _ in range(n)]   #달라지는 빗물의 양에 따른 방문여부를 확인할 visited리스트 초기화
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:   #빗물의 양 k보다 높이가 높고, 방문한 적이 없는 지역이라면
                bfs(i, j, k)    #bfs를 실행해 연결된 안전지대를 구함
                ans += 1    #하나의 안전지대 체크
    max_bfs = max(max_bfs, ans) #각 빗물의 양에 따른 ans(안전지대 갯수)중 최댓값을 저장
print(max_bfs)
