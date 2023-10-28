#n이 주어질 시 나선형 배치를 해본 결과
#오른쪽으로 n번 이동, 아래로 n-1번 이동, 왼쪽으로 n-1번 이동, 위로 n-2번 이동, 오른쪽으로 n-2번 이동...
#위의 패턴이 반복된다. 이를 그대로 코드로 옮겨 작성하면 index 초과가 발생하므로 해당 행의 boundary에 속한 수 이전까지 세어보았다.
#그 결과 n=4인 경우, 오른쪽으로 3번 이동(1, 2, 3), 아래로 3번 이동(4, 5, 6), 왼쪽으로 3번 이동(7, 8, 9), 위로 2번 이동(10, 11), 오른쪽으로 2번 이동(12, 13), 아래쪽으로 1번 이동(14), 왼쪽으로 1번 이동(15), 위쪽으로 1번 이동(14)가 된다.
#이를 그대로 코드로 옮겨 작성했다.

def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0 #현재 x, y 좌표
    num = 1 #현재 번호
    n -= 1  #반복횟수, index 초과 에러 방지 위해 n-1부터 시작
    for _ in range(n):    #가장 첫 줄, 오른쪽 이동
        answer[0][y] = num
        num += 1    #현재 번호 증가
        y += 1  #y좌표+1로 오른쪽 이동
    while n > 0:
        for _ in range(n):  #아래로 이동
            answer[x][y] = num
            num += 1
            x += 1
        for _ in range(n):  #왼쪽으로 이동
            answer[x][y] = num
            num += 1
            y -= 1
        n -= 1  #방향 2개당 n은 1씩 줄어든다.(이 부분에서 가장 마지막 이동 부분이 누락되므로 끝에 한번 더 처리해 준다.)
        for _ in range(n):  #위로 이동
            answer[x][y] = num
            num += 1
            x -= 1
        for _ in range(n):  #오른쪽으로 이동
            answer[x][y] = num
            num += 1
            y += 1
        n -= 1  #방향 2개당 n은 1씩 줄어든다.(이 부분에서 가장 마지막 이동 부분이 누락되므로 끝에 한번 더 처리해 준다.)
    answer[x][y] = num  #누락된 가장 마지막 수는 따로 처리해준다.
    return answer


----------------------------
[모범답안]

def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]   #오른쪽, 아래, 왼쪽, 위
    x, y, m = 0, 0, 0
    # 1 ~ N^2까지 처리
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        #배열 범위를 벗어난 경우 또는 answer의 해당 위치에 이미 값이 저장된 경우 처리
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move) #다음 방향으로 이동, 4개 벗어나는 경우 mod로 처리
        #좌표 이동
        y, x = y + move[m][0], x + move[m][1]
    return answer

