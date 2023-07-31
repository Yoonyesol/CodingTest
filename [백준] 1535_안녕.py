import sys
input=sys.stdin.readline
n = int(input())
L = [0]+list(map(int, input().split()))
J = [0]+list(map(int, input().split()))
dp = [[0]*101 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if L[i] <= j:
            #i번째 인사를 위해 i번째 인사만큼의 스테미나를 뺐을 때,
            #최적값에 i번째 인사의 기쁨값을 더한 값 
            # or i-1개의 인사를 가지고 구한 전 단계의 최적값 중 큰 것을 선택한다
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
        else:   # i번째 값이 체력보다 크다면 인사할 수 없음
            #i번째 체력을 뺀 i-1까지의 체력을 가지고 구해놓은 전 단계의 최대 기쁨값을 그대로 가져온다
            dp[i][j] = dp[i - 1][j]
print(dp[n][99])    #dp[n][100]은 체력을 모두 써서 사망한 것이므로, 그 이전까지의 값을 구함