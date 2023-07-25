import sys
input=sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
visited = [0 for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

def dfs(x):
    #x에 연결된 간선을 탐색(연결된 간선 == 1, 연결x 간선 == 0)
    for i in range(N):
        if visited[i] == 0 and graph[x][i]: #방문하지 않은 정점 + x에 연결된 간선
            visited[i] = 1  #방문처리
            dfs(i)  #현재 정점 i에 대해 연결된 정점이 존재하는지 깊이우선탐색 진행

for i in range(N):
    dfs(i)  #세로방향으로, 처음부터 끝까지 dfs 실행해서 연결된 간선 탐색
    for j in range(N):  #매번 dfs 종료 후에는 해당 행의 방문한 간선을 출력
        print(visited[j], end=' ')
    print()
    visited = [0 for _ in range(N)]

--------------------

import sys
from collections import deque
input=sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start) #시작 정점을 queue에 삽입
    visited = [0]*n #방문한 노드를 저장할 리스트 생성 및 초기화
    while queue:    #queue가 빌 때까지(가능한 모든 이동가능한 경로를 찾을 때까지)
        node = queue.popleft()  #먼저 들어온 값부터 꺼냄
        for i in graph[node]:   #현재 노드에 연결된 모든 노드를 확인
            if not visited[i]:  #방문하지 않은 노드가 있다면
                visited[i] = 1  #방문처리
                queue.append(i) #현재 노드에서부터 다른 노드로의 경로도 확인하기 위해 현재 노드를 queue에 저장
    print(*visited) #방문처리된 결과를 출력(시작노드에서 방문가능한 경로라면 1로 표시되고, 아닌 경우 값이 초기화 값인 0으로 유지된다)

n = int(input())
graph = [[] for _ in range(n)]  #bfs로 순회할 그래프 생성 및 초기화
for i in range(n):
    arr = list(map(int, input().split()))   #행렬을 한줄씩 리스트 형태로 입력받기
    for j in range(n):  #입력받은 리스트의 원소를 확인
        if arr[j] == 1: #리스트의 원소가 1이라면,
            graph[i].append(j)  #i에서 j로 이동하는 것이 가능하다는 뜻이므로 그래프에 이동가능 경로 표시(유향그래프이므로, graph[j].append(i)는 진행하지 않는다.)

for i in range(n):  #그래프의 모든 정점에 대해 bfs 실행
    bfs(i)  #시작노드는 현재 정점