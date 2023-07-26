import sys
input=sys.stdin.readline
n = int(input())
pan = [list(input()) for _ in range(n)]

def check():    #배열 전체를 검사하여 먹을 수 있는 사탕 수의 max를 구하는 함수
    max_cnt = 0 #먹을 수 있는 사탕의 최대값. 0으로 초기화
    for i in range(n):
        cnt = 1 #동일한 사탕의 수를 세는 변수
        for j in range(n-1):   #각 행마다 검사
            if pan[i][j] == pan[i][j+1]:    #오른쪽 사탕과 비교해서 동일한 사탕인 경우
                cnt += 1    #카운트+1
                max_cnt = max(max_cnt, cnt) #최대값 업데이트
            else:   #동일한 경우를 모두 카운팅하고, 동일하지 않은 경우가 나오면 카운팅 변수를 초기화한다.
                cnt = 1
        cnt = 1
        for j in range(n-1):   #각 열마다 검사
            if pan[j][i] == pan[j+1][i]:    #아래 사탕과 비교해서 동일한 사탕인 경우
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt
max_cnt = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:   #가로 체크
            pan[i][j], pan[i][j+1] = pan[i][j+1], pan[i][j] #오른쪽 사탕과 바꾸기
            max_cnt = max(max_cnt, check()) #먹을 수 있는 사탕의 최대값을 체크하여 업데이트
            pan[i][j], pan[i][j + 1] = pan[i][j + 1], pan[i][j] #원상복귀
        if i + 1 < n:   #세로 체크
            pan[i][j], pan[i+1][j] = pan[i+1][j], pan[i][j] #아래 사탕과 바꾸기
            max_cnt = max(max_cnt, check())
            pan[i][j], pan[i+1][j] = pan[i+1][j], pan[i][j]
print(max_cnt)

-------------------------

import sys
input=sys.stdin.readline
n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]

def maxCandy():
    max_cnt = 0 #최대 cnt값을 저장하는 변수
    for i in range(n):
        cnt = 1 #동일한 사탕의 갯수를 카운팅할 변수
        for j in range(n - 1):
            if candy[i][j] == candy[i][j+1]:    #오른쪽 사탕과 비교
                cnt += 1    #양쪽 사탕이 동일한 경우 카운팅
                max_cnt = max(max_cnt, cnt) #동일한 사탕 최대갯수 업데이트
            else:
                cnt = 1 #한 줄의 중간에 동일하지 않은 사탕이 껴있을 때, cnt 초기화하고 다시 세기
        cnt = 1
        for j in range(n - 1):
            if candy[j][i] == candy[j+1][i]:    #아래쪽 사탕과 비교
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt

max_candy = 0   #동일한 사탕의 갯수 중 가장 큰 값을 저장하는 변수
for i in range(n):
    for j in range(n-1):
        if candy[i][j] != candy[i][j+1]:    #현재 사탕의 오른쪽 사탕 검사, 동일하지 않다면
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] #두 사탕의 위치를 바꿈
            max_candy = max(maxCandy(), max_candy)  #현 위치에서 동일한 사탕의 최대갯수 구하기
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] #원복
    for j in range(n-1):
        if candy[j][i] != candy[j+1][i]:    #현재 사탕의 아래쪽 사탕 검사
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
            max_candy = max(maxCandy(), max_candy)
            candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
print(max_candy)