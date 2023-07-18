import sys
input=sys.stdin.readline
n, k = map(int, input().split())    #n개 중 k개를 뽑기
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if i == j or j == 0:    #파스칼의 삼각형의 1 조건
            dp[i][j] = 1
        else:   #이항계수 점화식 그대로 코드화
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007
print(dp[n][k]%10007)

------------------------

import sys
input=sys.stdin.readline
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(k+1):
        if j==0 or i==j:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007
print(dp[n][k]%10007)


