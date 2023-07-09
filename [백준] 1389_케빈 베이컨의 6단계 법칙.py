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