from collections import deque
import sys
input=sys.stdin.readline
n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs(idx):
    queue = deque()
    queue.append(idx)
    visited[idx] = 1
    while queue:
        x = queue.popleft()
        for i in friends[x]:
            if not visited[i]:
                visited[i] = visited[x]+1
                queue.append(i)
arr = []
for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    bfs(i)
    arr.append(sum(visited))
print(arr.index(min(arr))+1)

------------------

import sys
from collections import deque
input=sys.stdin.readline
n, m = map(int, input().split())
bacon = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    bacon[a].append(b)
    bacon[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = 1
    while queue:
        x = queue.popleft() #큐에서 가장 앞 원소 x를 꺼낸다
        for i in bacon[x]:  #x의 이웃한 노드 i를 모두 확인한다.
            if not visited[i]:  #이웃한 노드 중 아직 방문하지 않은 노드의 경우
                #start - i 간 거리 체크(기존에 체크해둔 거리+1씩 늘려나가며 체크)
                visited[i] = visited[x]+1
                queue.append(i)
arr = []    #1부터 n까지 각 수를 시작점으로 하는 케빈베이컨의 수를 담을 배열
for i in range(1, n+1):
    visited = [0 for _ in range(n + 1)]
    bfs(i)
    arr.append(sum(visited))    #start인 i 노드에서 각 원소까지의 거리를 체크한 visited의 총합을 arr에 삽입
print(arr.index(min(arr))+1)    #가장 작은 수의 인덱스+1(1 based로 만들기 위해)