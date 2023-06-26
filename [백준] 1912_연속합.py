import sys
input=sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp =[0]*n   #dp배열 생성 및 초기화
for i in range(n):
    # 가장 처음 원소는 그대로 넣어줌
    if i == 0:  dp[0] = arr[0]
    else:
        #(이전 최대 연속합+현재값, 현재값)을 비교해서 더 큰 수를 dp테이블에 넣어준다
        dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))