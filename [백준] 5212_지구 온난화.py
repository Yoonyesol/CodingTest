import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
minX, minY = 1e9, 1e9   #섬의 가장 작은 x좌표, y좌표
maxX, maxY = 0, 0   #섬의 가장 큰 x좌표, y좌표

def visit(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    cnt = 0 #주변이 3개 이상의 바다로 둘러싸였는지 확인하기 위한 카운터
    global minX
    global minY
    global maxX
    global maxY

    for i in range(4):  #4면을 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= r or nx < 0 or ny >= c or ny < 0:  #배열을 벗어난 부분도 바다
            cnt += 1
            continue
        if arr[nx][ny] == '.':  #바다인 경우 체크
            cnt += 1

    if cnt >= 3:    #삼면이나 사면이 바다로 둘러싸인 경우 이 섬은 물에 잠긴다.
        arr[x][y] = 'a' #.이나 X가 아닌 아무 문자로 변경
    else:   #그렇지 않은 경우 물레 잠기지 않는다.
        minX = min(minX, x) #물에 잠기지 않고 존재하는 섬의 가장 작은 x좌표를 구한다.
        minY = min(minY, y) #존재하는 섬의 가장 작은 y좌표를 구한다.
        maxX = max(maxX, x) #존재하는 섬의 가장 큰 x좌표를 구한다.
        maxY = max(maxY, y) #존재하는 섬의 가장 큰 y좌표를 구한다.

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'X':    #섬인 경우
            visit(i, j) #바다로 변할 섬인지 확인

for i in range(minX, maxX+1):   #가장 작은 섬의 x좌표부터 가장 큰 x좌표까지 방문
    for j in range(minY, maxY+1):   #섬의 가장 작은 y좌표부터 가장 큰 y좌표까지 방문
        if arr[i][j] == 'a':    #만약 해당 섬이 물에 잠길 섬으로 표시되어 있다면
            arr[i][j] = '.' #바다로 변경
        print(arr[i][j], end="")    #차례로 출력
    print()