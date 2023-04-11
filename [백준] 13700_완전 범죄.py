import sys
from collections import deque

def bfs(cnt, x):
    queue = deque()
    queue.append((cnt, x))
    while queue:
        cnt, x = queue.popleft()
        dx = [x-b, x+f]
        for nx in dx:
            if nx >= n or nx < 0:
                continue
            if game[nx] == "p":
                continue
            if game[nx] == "h":
                return cnt
            game[nx] = "p"
            queue.append((cnt+1, nx))
    return "BUG FOUND"
    
n, s, d, f, b, k = map(int, sys.stdin.readline().split())
game = ["t"] * n

#털린 금은방
game[s-1] = "g"

#도둑의 집
game[d-1] = "h"

temp = []
#경찰서 배치
temp = list(map(int, sys.stdin.readline().split()))
for i in temp:
    game[i-1] = "p"

cnt = 1
for i in range(n):
    if game[i] == "g":
        print(bfs(cnt, i))



