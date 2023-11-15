import sys
input=sys.stdin.readline

dp = [1] * 10001    #1로만 이루어진 경우의 수

for i in range(2, 10001):
    dp[i] += dp[i-2]    #i-2의 경우에 2를 추가하여 만들 수 있는 경우의 수

for i in range(3, 10001):
    dp[i] += dp[i-3]    #i-3의 경우에 3을 추가하여 만들 수 있는 경우의 수

t = int(input().rstrip())
for i in range(t):
    print(dp[int(input().rstrip())])
