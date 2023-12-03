import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

#북동남서 후진 방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

#방문했는지 체크하는 리스트
visited = [[0] * m for _ in range(n)]

#첫번째 좌표 방문
visited[r][c] = 1
cnt = 1 #방문한 횟수 카운트
while True:
    flag = 0    #주위 4방향에 청소가 안 된 구역이 있는지 확인하는 플래그. 매번 0으로 초기화해 이번 좌표 근처 4좌표 중 청소된 곳이 있는지 확인하게 해준다.
    for _ in range(4):
        d = (d + 3) % 4 #현재 좌표에서 90도씩 왼쪽으로 돌림
        nr = r + dr[d]  #90도 돌린 r 좌표
        nc = c + dc[d]  #90도 돌린 c 좌표
        if nr >= n or nr < 0 or nc >= m or nc < 0 or arr[nr][nc] or visited[nr][nc]:    #인덱스 범위를 벗어나거나 벽이거나 이미 청소를 마친 좌표라면
            continue    #아래 코드 실행x 건너뜀
        visited[nr][nc] = 1 #청소 표시
        cnt += 1    #청소 횟수 +1
        r, c = nr, nc   #현재 좌표 이동
        flag = 1    #청소 진행했다는 사실 표시
        break   #현재 d에서 청소를 마쳤으므로, 종료하고 nr, nc에서 다음 청소 구역을 찾기 위해 현재 for문 빠져나감

    if flag: continue   #청소가 진행됐다면 아래 코드 실행x, 청소한 구역이 없을 때 아래 코드 실행
    if arr[r-dr[d]][c-dc[d]] == 1:  #현재 방향에서 후진한 곳이 벽이라면
        print(cnt)  #카운팅한 횟수를 출력하고
        break   #작동 종료
    else:   #벽이 아니라면
        r, c = r-dr[d], c-dc[d] #후진한 좌표로 r, c 초기화