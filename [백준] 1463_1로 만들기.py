import sys
input=sys.stdin.readline
n = int(input())
dp = [0] * (n+1)    #1 based index
for i in range(2, n+1): #1의 최소 연산 수는 0이므로, 2부터 연산 진행
    dp[i] = dp[i-1] + 1 #1을 빼는 경우 최소 연산의 수(연산의 횟수를 체크하기 위해 +1)
    if i % 3 == 0:  #3으로 나누어 떨어지면
        dp[i] = min(dp[i], dp[i//3]+1)  #1을 빼는 경우와 3으로 나눈 경우 중, 연산의 수가 더 적은 것을 택한다
    if i % 2 == 0:  #2로 나누어 떨어지면
        dp[i] = min(dp[i], dp[i//2]+1)  #1을 빼는 경우와 2으로 나눈 경우 중, 연산의 수가 더 적은 것을 택한다
print(dp[n])