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