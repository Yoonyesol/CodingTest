import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
maxWidth = min(n, m)
ans = 0

for i in range(n):
    for j in range(m):
        for k in range(maxWidth):
            if (i+k) < n and (j+k) < m and (arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]):
                ans = max(ans, (k+1)**2)
print(ans)