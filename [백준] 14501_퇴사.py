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


---------------------------------


import sys
input=sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    # arr[i][0]: 상담일수
    # arr[i][1]: 상담금액

#idx: 현재날짜, charge: 총 보수
def dfs(idx, charge):
    global ans
    if idx == n:    #퇴사일
        ans = max(ans, charge)  #현재값 ans와 여태까지 더한 총 보수 중 더 큰 수로 업데이트
        return ans
    #상담을 하는 경우
    if idx + arr[idx][0] <= n:   #퇴사일을 벗어나지 않는 선에서 상담진행
        dfs(idx+arr[idx][0], charge+arr[idx][1])    #상담일동안 상담을 하고, 보수 추가(상담일수 안에 다른 상담은 하지 않는다)
    #상담을 하지 않는 경우
    dfs(idx+1, charge)  #일수+1, 보수는 그대로

ans = 0 #최대 수익을 구해야 하므로 0으로 초기화
dfs(0, 0)   #함수 실행
print(ans)  #함수 실행결과로 나온 ans값 출력

#<시간복잡도> 최대 상담일수(N)가 15일이므로, 상담을 하는 경우와 하지 않는 경우를 탐색하면 시간 복잡도는 O(2^15)이다.
#만약 N값이 50정도로 커진다면 시간초과 발생. dp로 접근해야 한다.
#<+> ans값을 max로 정해주어야 가장 큰 수를 뽑아낼 수 있는데 ans = charge로 코드를 짜버려서 헤맸다.
#매번 재귀를 종료하며 charge값은 달라지기 때문에, max를 이용해 최댓값을 구해주어야 한다.