import sys
com = int(sys.stdin.readline())
ssang = int(sys.stdin.readline())
graph = [[] for _ in range(com + 1)]
visited = [False] * (com + 1)
global answer
answer = 0

for _ in range(ssang):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  global answer
  visited[v] = True
  answer += 1
  for i in graph[v]:
    if not visited[i]:
      dfs(i)
      
dfs(1)
print(answer - 1)