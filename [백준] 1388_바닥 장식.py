import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
bang = []
for _ in range(n):
    bang.append(list(sys.stdin.readline().rstrip()))

def dfs1(y, x):
    if x >= m or y >= n or x < 0 or y < 0:
        return
    if bang[y][x] == "-":
        bang[y][x] = "o"
        for i in [-1, 1]:
            nx = x + i
            dfs1(y, nx)
def dfs2(y, x):
    if x >= m or y >= n or x < 0 or y < 0:
        return
    if bang[y][x] == "|":
        bang[y][x] = "o"
        for i in [-1, 1]:
            ny = y + i
            dfs2(ny, x)
cnt = 0
for i in range(n):  #세로(y)
    for j in range(m):  #가로(x)
        if bang[i][j] == "-":
            dfs1(i, j)
            cnt += 1
        elif bang[i][j] == "|":
            dfs2(i, j)
            cnt += 1
print(cnt)