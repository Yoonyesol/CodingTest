T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(m):
        index, num = map(int, input().split())
        arr = arr[:index] + [num] + arr[index:]
    print('#{} {}'.format(test_case, arr[l]))