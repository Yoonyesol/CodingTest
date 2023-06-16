import sys
input=sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [0 for _ in range(n)]

#n//2명 뽑아서 true(1)로 넘기기
def dfs(cnt, idx):
    global score
    a_sum, b_sum = 0, 0
    if cnt == 0:    #N//2명 뽑기 완료
        #print(visited)
        #뽑은 배열 확인해서 점수 가산
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if visited[i] and visited[j]:   #둘 다 1인 경우(a팀)
                    a_sum += arr[i][j]
                elif not visited[i] and not visited[j]:   #둘 다 0인 경우(b팀)
                    b_sum += arr[i][j]
        #print(a_sum, b_sum)
        score = min(score, abs(a_sum-b_sum))    #더 작은 수로 업데이트
        return score
    #조합 뽑기
    for i in range(idx, n):
        visited[i] = 1
        dfs(cnt-1, i+1)
        visited[i] = 0	   #다음 조합을 위해 원상복귀

score = sys.maxsize #두 팀의 점수차이
dfs(n//2, 0)
print(score)