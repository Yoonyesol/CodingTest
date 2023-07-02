import sys
from collections import deque
input=sys.stdin.readline
m, n, k = map(int, input().split()) #m:세로, n:가로, k:직사각형 개수

arr = [[0]*n for _ in range(m)] #영역 배열
for _ in range(k):  #사각형의 좌표를 받아 해당하는 부분의 배열 원소를 1로 채운다
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2): #x좌표의 모든 부분에 대해
        for j in range(y1, y2): #y좌표에 해당하는 배열 원소를 1로 채운다
            arr[j][i] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    global ans
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1 #다음번 방문에 또다시 체크되지 않도록 방문처리
                ans += 1    #빈 영역 개수 체크
                queue.append((nx, ny))

area = 0
ans_arr = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:  #빈 영역일 경우
            ans = 0
            bfs(i, j)
            area += 1   #나누어진 총 빈 영역 개수
            if ans == 0:    #ans가 0인 경우에도 if문에 들어온 이상 빈 영역이 1개 존재한다는 뜻이므로 1을 ans 배열에 추가
                ans_arr.append(1)
            else:   #ans가 0이 아닌 경우 bfs를 통해 구한 ans 값을 그대로 ans 배열에 넣는다
                ans_arr.append(ans)
print(area)
print(' '.join(map(str, sorted(ans_arr))))  #오름차순 정렬하여 출력

