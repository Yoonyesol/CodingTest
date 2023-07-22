import sys
input=sys.stdin.readline
n = int(input())
dp = [0, 1, 0, 1, 1, 1, 1]  #n의 갯수에 따른 승리결과(상근이 승리가 1, 패배가 0)
if n > 6:   #n이 6보다 큰 경우는 바로 dp값에 따라 값을 출력
    for i in range(7, n+1):
        # 각 항의 값이 1인 경우, 각 턴에 상근이가 돌을 가져갔다는 의미. 
        # 상근이 다음 턴에 남은 1개 or 3개 or 4개의 돌을 창영이가 가져갈 수 있는 경우의 수. 
        # 즉, 상근이가 패배하는 경우
        if dp[i-1]+dp[i-3]+dp[i-4] == 3:    
            dp.append(0)    #해당 턴은 창영이의 승리
        else:
            dp.append(1)
if dp[n]:   #값이 1인 경우, 상근이의 승리
    print("SK")
else:
    print("CY")