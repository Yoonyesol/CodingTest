import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
chon = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    c, d = map(int, sys.stdin.readline().split())
    chon[c].append(d)
    chon[d].append(c)
visited = [-1 for _ in range(n+1)]
visited[a] = 0

def dfs(start):
    for i in chon[start]:
        if visited[i] == -1:
            visited[i] = visited[start] + 1
            dfs(i)


def bfs(start):
    queue = []
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for i in chon[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)

dfs(a)
# bfs(a)
print(visited[b])