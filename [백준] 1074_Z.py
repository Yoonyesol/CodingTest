import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def dfs(row, col, size):
    global total
    if size == 1:   #1x1이라 더 이상 쪼갤 수 없을 때
        if col == c and row == r:   #정확한 좌표를 찾았을 때 결과 출력
            print(total)
            return
        #정확한 좌표를 찾지 못 했을 때 결과값 1 증가
        total += 1
        return

    #현재 크기의 4등분 중 어느 영역에 위치하는지 확인
    half = size // 2
    if r < half + row and c < half + col:   #1사분면
        dfs(row, col, half)
    elif r < half + row and c >= half + col:    #2사분면
        total += half * half    #2사분면까지 도달하는데 카운팅한 원소 개수(1사분면 분량)
        dfs(row, col+half, half)    #이미 해당 좌표가 존재하지 않는다는 것을 확인한 위치는 확인할 구역에서 제외하고 그 외의 영역을 확인
    elif r >= half + row and c < half + col:    #3사분면
        total += half * half * 2    #3사분면까지 도달하는데 카운팅한 원소 개수(1사분면 2개 분량)
        dfs(row+half, col, half)
    elif r >= half + row and c >= half + col:   #4사분면
        total += half * half * 3    #4사분면까지 도달하는데 카운팅한 원소 개수(1사분면 3개 분량)
        dfs(row+half, col+half, half)

total = 0
dfs(0, 0, 2**n)