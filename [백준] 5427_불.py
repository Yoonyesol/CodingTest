import sys
from collections import deque
input=sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        if visited[x][y] != "F":    #현재 위치가 불이 붙지 않은 좌표라면
            flag = visited[x][y]    #flag는 현재 위치
        else:   #불이 붙은 좌표라면
            flag = "F"  #flag를 F로 설정

        for i in range(4):  #상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= h or nx < 0 or ny >= w or ny < 0:  #배열의 범위를 넘어선 경우, 탈출에 성공한 것
                if flag != "F": #현재 플래그가 F가 아니라면(불 붙은 좌표로 인해 불이 넘어오지 않음)
                    return flag + 1 #탈출 성공(현재 좌표의 값을 리턴)
                continue    #배열의 범위를 벗어난 경우 아래 코드는 실행x
            # 아직 방문하지 않은 좌표이고, 해당 좌표가 빈공간이나 시작좌표라면
            if visited[nx][ny] == -1 and (building[nx][ny] == "." or building[nx][ny] == "@"):  
                if flag == "F": #현재 플래그가 F라면(불 붙은 좌표x,y로 인해 이번 타임에 nx, ny에 불이 넘어옴)
                    visited[nx][ny] = flag  #visited[nx][ny]에도 불이 붙었음을 표시
                else:   #현재 플래그가 F가 아니라면
                    visited[nx][ny] = flag + 1  #기존 좌표값에 +1
                queue.append((nx, ny))  #다음 좌표를 탐색하기 위해 큐에 현재 좌표를 저장
    return "IMPOSSIBLE" #모든 좌표를 돌았는데도 탈출하지 못했다면, impossible 리턴

n = int(input())
for tc in range(n):
    w, h = map(int, input().split())
    building = []
    visited = [[-1] * w for _ in range(h)]
    queue = deque()

    for i in range(h):
        building.append(list(input().rstrip())) #한 줄씩 입력받아 building 배열에 저장
        for j in range(w):  #입력받은 한 줄에 대해 반복
            if building[i][j] == "@":   #상근이 시작위치
                visited[i][j] = 0
                start = (i, j)  #시작위치 저장
            elif building[i][j] == "*": #불
                visited[i][j] = "F" #불이 붙은 좌표 표시
                queue.append((i, j))    #큐에 불의 좌표 저장, 상근이는 이제 곧 불이 붙으려는 칸으로 이동할 수 없으므로, 불을 맨앞에 넣고 상근이 위치를 마지막에 넣어야 한다.
    queue.append(start) #상근이 위치를 마지막에 저장
    print(bfs())    #bfs실행하고 결과를 출력
