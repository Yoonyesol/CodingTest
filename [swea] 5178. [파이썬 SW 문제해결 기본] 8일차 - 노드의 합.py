T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().split())
    arr = [0 for _ in range(n+2)]
    for _ in range(m):
        node, num = map(int, input().split())
        arr[node] = num
    for i in range(len(arr)-1, 2, -1):
        if i % 2 == 0 and arr[i] != 0:
            par = (i + i+1) // 4
            if par == l:
                ans = arr[i] + arr[i+1]
                break
            else:
                arr[par] = arr[i] + arr[i+1]
    print('#{} {}'.format(test_case, ans))