#itertools 라이브러리
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
ans = 0 #공식 대입 결과 가장 큰 값(정답)을 저장할 변수

for i in list(permutations(arr)):   #리스트의 원소가 이룰 수 있는 전체 순열 확인
    total = 0   #해당 순열에서 공식 대입값을 구할 변수
    for j in range(n-1):    #공식을 이용해 현재 순열의 결과값을 구한다.
        total += abs(i[j] - i[j+1])
    ans = max(ans, total)   #매번 구한 순열과 이전까지의 최대값 중 더 큰 것을 정답 변수에 저장
print(ans)


------------------------------
#재귀
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
visited = [False] * n
ans = 0

def dfs(permu):
    global ans
    if len(permu) == n: #모든 원소의 순서를 정했다면
        total = 0 
        for i in range(n-1):    #공식에 전체 원소를 넣고 결과를 확인
            total += abs(permu[i] - permu[i+1])
        ans = max(ans, total)
        return
    #전형적인 백트래킹 코드. 이해는 쉽지 않지만 우선 외우자
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            permu.append(arr[i])
            dfs(permu)
            visited[i] = False
            permu.pop() #원소를 제거하고 그 공간에 다른 원소를 넣는다.
dfs([])
print(ans)