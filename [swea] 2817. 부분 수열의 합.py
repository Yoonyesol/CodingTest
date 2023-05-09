def dfs(depth, hap):
    global ans
    if hap == k:
        ans += 1
        return
    if depth == n:
        return
    a = arr[depth]
    dfs(depth+1, a+hap) #해당 수 선택하는 경우
    dfs(depth+1, hap) #해당 수 선택하지 않는 경우

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print("#{} {}".format(test_case, ans))