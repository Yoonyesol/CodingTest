import sys
input = sys.stdin.readline

n, tScore, p = map(int, input().split())
cnt = 1 #등수

if n > 0:
    scores = list(map(int, input().split()))    #점수 리스트

    # 랭킹 리스트가 꽉 차 있고 새 점수가 이전 점수보다 나쁘다면
    if n == p and tScore <= scores[-1]:
        cnt = -1    #점수가 바뀌지 않음
    else:   #새 점수가 이전 점수보다 좋다면
        for i in scores:
            if tScore < i:  #등수 매기기
                cnt += 1
            else:
                break
print(cnt)