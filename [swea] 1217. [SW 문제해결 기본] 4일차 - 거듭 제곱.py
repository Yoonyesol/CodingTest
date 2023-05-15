def dfs(n, m, cnt):
    if cnt == m:
        return n
    return n * dfs(n, m, cnt+1)
T = 10
for test_case in range(1, T+1):
    int(input())
    n, m = map(int, input().split())
    print("#{} {}".format(test_case, dfs(n, m, 1)))