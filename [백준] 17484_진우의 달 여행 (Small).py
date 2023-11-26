import sys
input = sys.stdin.readline

n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]

direction = [-1, 0, 1]  #이동할 y좌표 방향

def dfs(col, row, visited, total, minVal):  #세로, 가로, 방문한 방향, 총연료비, 가장 작은 연료비
    if col == n-1:  #더 이상 진행할 행이 없는 경우
        return min(minVal, total)   #현재 텀의 총 연료비와 기존에 저장되어 있던 가장 작은 연료비 중 더 작은 것 리턴
    for i in direction: #3가지 방향을 모두 돈다.
        if i == visited:    #이전에 진행했던 방향은 가지 않는다(문제 조건)
            continue
        if col >= n or col < 0 or row+i >= m or row+i < 0:  #인덱스 범위 벗어나는 경우도 가지 않는다.
            continue
        minVal = dfs(col+1, row+i, i, total+space[col+1][row+i], minVal)    #dfs를 통해 col, row를 늘려가며 minVal을 구한다.
    return minVal   #각 호출에서 찾은 최소 연료비를 반환. 재귀 호출에서 마지막 행에 도달하면 min(minVal, total)을 반환하고, 이 값이 상위호출 minVal에 저장된다.

minVal = 1e9
for i in range(m):
    # 각 시작지점에 대해 dfs를 실행하고 매번 return 받은 최소연료비 중 가장 작은 값을 minVal에 저장
    minVal = min(dfs(0, i, 2, space[0][i], minVal), minVal) #2는 -1, 0, 1이 아닌 수 중 아무거나 넣은 것

print(minVal)