#부분 집합
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

subset = [[]]
cnt = 0
for i in arr:   #arr의 모든 원소에 대해 반복
    for j in range(len(subset)):    #subset 리스트의 모든 원소에 대해 for문 돌기
        a = subset[j]+[i]   #기존 존재하는 원소집합에 i를 더한 새로운 원소집합
        subset.append(subset[j]+[i])    #새로운 부분집합 리스트 추가
        if sum(a) == s: #매번 만들어진 부분집합의 전체 원소합을 구해 s와 같다면 카운팅
            cnt += 1
print(cnt)

---------------------------------------
#재귀
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

def dfs(idx, result):
    global cnt
    if idx >= n:    #인덱스를 벗어난다면 모든 원소를 체크했다는 의미이므로 return
        return
    if result + arr[idx] == s:  #result에 현재 인덱스의 수를 더했을 때 그 결과가 s라면 cnt 카운팅
        cnt += 1

    dfs(idx+1, result)  #현재 인덱스의 수를 선택하지 않은 부분수열
    dfs(idx+1, result + arr[idx])   #현재 인덱스의 수를 선택한 부분수열

cnt = 0
dfs(0, 0)
print(cnt)