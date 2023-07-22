import sys
input=sys.stdin.readline
n = int(input())
dp = [0] * (n+1)    #1 based index
for i in range(2, n+1): #1의 최소 연산 수는 0이므로, 2부터 연산 진행
    dp[i] = dp[i-1] + 1 #1을 빼는 경우 최소 연산의 수(연산의 횟수를 체크하기 위해 +1)
    if i % 3 == 0:  #3으로 나누어 떨어지면
        dp[i] = min(dp[i], dp[i//3]+1)  #1을 빼는 경우와 3으로 나눈 경우 중, 연산의 수가 더 적은 것을 택한다
    if i % 2 == 0:  #2로 나누어 떨어지면
        dp[i] = min(dp[i], dp[i//2]+1)  #저장된 최소값과 2으로 나눈 경우 중, 연산의 수가 더 적은 것을 택한다
print(dp[n])

------------------------

import sys
input=sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1   #n에서 1을 뺀 경우. 계산횟수가 1회 늘었으므로 이전까지의 연산횟수+1
    # i가 3으로 나눠지는 경우, i//3에서 3을 곱한 값이 현재 i값이다.
    # 따라서 dp[i]에 저장가능한 경우의 수 중 하나는 dp[i//3]+1(3곱한 연산횟수+)
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])  #두 값을 비교해 연산횟수가 더 작은 값을 dp[i]에 저장
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i]) #저장된 최소값과 2로 나누어 연산한 계산횟수 중 더 작은 값을 dp[i]에 저장
print(dp[n])
