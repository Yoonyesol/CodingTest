T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(1, n+1):
        if i not in arr:
            ans.append(i)
    print("#{} {}".format(test_case, ' '.join(map(str, ans))))