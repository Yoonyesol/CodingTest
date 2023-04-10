import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(n+1)]

def dfs(v):
    visited[v] = 1
    # print(v, end= " ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

answer = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        answer += 1
print(answer)