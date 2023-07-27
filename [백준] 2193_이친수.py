import sys
input=sys.stdin.readline
n = int(input())
if n == 1:  #n이 1인 경우 for문 내의 range(3, n+1)를 수행할 수 없으므로
    print(1)    #그냥 1을 출력
else:
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i-2]
    print(dp[n])
    
# n = 1: 1
# n = 2: 10
# n = 3: 100, 101
# n = 4: 1000, 1001, 1010
# n = 5: 10000, 10001, 10010, 10100, 10101
# dp = [1, 1, 2, 3, 5, 8, 13...] => 규칙을 확인해 점화식을 짠다.

------------------------------

import sys
input=sys.stdin.readline
n = int(input())
dp = [0, 1, 1]	#초기값
for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])	#점화식을 통해 매번 새로운 수를 리스트에 저장
print(dp[n])