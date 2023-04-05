import sys
N, M, V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
      i.sort()

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(i)


def BFS(start):
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited = [False] * (N+1)
DFS(V)
print()
queue = []
visited = [False] * (N+1)
BFS(V)