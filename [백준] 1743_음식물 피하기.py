import sys
from collections import deque
input=sys.stdin.readline
n, m, k = map(int, input().split())
arr = [["."]*m for _ in range(n)]

for _ in range(k):  #음쓰 좌표에 '#'놓기
    a, b = map(int, input().split())
    arr[a-1][b-1] = "#"

dx = [0, 0, 1, -1]  #x의 상하좌우 좌표
dy = [1, -1, 0, 0]  #y의 상하좌우 좌표
def bfs(y, x):
    global ans  #음쓰카운팅할 변수
    queue = deque()
    queue.append((y, x))    #초기 방문 좌표
    while queue:
        y, x = queue.pop()
        arr[y][x] = '.' #방문한 좌표는 .으로 처리해 다시 방문하지 않게 한다
        for i in range(4):  #상하좌우 좌표를 살핀다
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0:  #인덱스에러 방지
                continue
            if arr[ny][nx] == ".":  #이동한 좌표의 값이 "."인 경우 아무런 처리도 하지 않는다
                continue
            if arr[ny][nx] == "#":  #이동한 좌표의 값이 "#"인 경우 해당 좌표에서 또 다시 상하좌우를 방문하여 또 다른 음쓰를 찾는다
                ans += 1    #음쓰 발견 카운팅
                arr[ny][nx] = '.'   #한번 지나온 길은 방문처리
                queue.append((ny, nx))  #현재 좌표의 상하좌우를 살필 수 있도록 queue에 현재 좌표를 넣어준다.
max_ans = 0 #가장 큰 음쓰를 찾는 변수
for i in range(n):  #세로
    for j in range(m):  #가로
        if arr[i][j] == "#":    #arr에서 음쓰를 찾은 경우
            ans = 1 #음쓰 1개 찾음 카운팅
            bfs(i, j)   #현재 좌표를 기준으로 bfs를 실행해 근처의 이어진 음쓰를 모두 찾는다.
            max_ans = max(max_ans, ans) #기존 max_ans와 새로 구해진 ans의 값 중 큰 값을 max_ans에 대입
print(max_ans)
