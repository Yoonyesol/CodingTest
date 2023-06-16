import sys
input=sys.stdin.readline
n = int(input())
arr = []
dp = [0 for _ in range(n+1)]
for _ in range(n):
    t, p = map(int, input().split())
    arr.append([t, p])

for i in range(n):
    #print(i)
    for j in range(i+arr[i][0], n+1):   #i번째 날에 상담 시작 ~ 마지막 날까지 카운트
        #print(j, dp[j], dp[i]+arr[i][1])
        if dp[j] < dp[i]+arr[i][1]: #더 큰 값으로 업데이트(새로운 상담 진행, 수익+)
            dp[j] = dp[i] + arr[i][1]
        #dp[j] = max(dp[j], dp[i]+arr[i][1])
        #print(dp)

print(dp[-1])   #최대 수익 체크