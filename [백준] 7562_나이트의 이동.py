import sys
from collections import deque
input=sys.stdin.readline
tc = int(input())
for _ in range(tc):
    l = int(input())    #보드 사이즈
    current_xy = list(map(int, input().split()))    #현재 좌표
    goal = list(map(int, input().split()))  #목표 좌표
    if current_xy == goal:  #현재 좌표==목표 좌표인 경우, 0을 출력하고 다음 TC로 넘어감
        print(0)
        continue

    arr = [[0]*l for _ in range(l)] #0으로 초기화된 보드 배열
    dx = [1, -1, 2, -2, 2, -2, 1, -1]   #이동 좌표(X)
    dy = [-2, -2, -1, -1, 1, 1, 2, 2]   #이동 좌표(Y)

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        arr[x][y] = 1   #초기좌표 1로 방문처리
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]  #방문할 좌표(X)
                ny = y + dy[i]  #방문할 좌표(Y)
                if nx >= l or nx < 0 or ny >= l or ny < 0:  #배열의 범위 벗어난 경우 처리
                    continue
                if arr[nx][ny] != 0:    #이미 방문한 적 있는 좌표는 방문하지 X(최단거리 구해야 하므로 중복 피해야 함)
                    continue
                arr[nx][ny] = arr[x][y] + 1 #여태껏 방문한 좌표의 수+1을 arr[nx][ny]에 저장
                if nx == goal[0] and ny == goal[1]: #방문할 좌표가 목표 좌표라면
                    return arr[nx][ny]-1    #마지막 방문처리(+1)한 것 제외하고 arr[nx][ny] 리턴
                queue.append((nx, ny))  #리턴되지 않을 시, 다음 방문을 위해 현재 좌표를 큐에 저장
    print(bfs(current_xy[0], current_xy[1]))    #현재좌표X,Y를 시작좌표로 삼아 BFS실행