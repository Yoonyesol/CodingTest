T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    graph = [[]*(n+1) for _ in range(n+1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def dfs(x, cnt):
        global ans
        ans = max(ans, cnt)
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                dfs(i, cnt+1)
        visited[x] = False

    ans = 1
    for j in range(1, n+1):
        dfs(j, 1)
    print("#{} {}".format(test_case, ans))