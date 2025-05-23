T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    arr_sum = arr[:k]
    print('#{} {}'.format(test_case, sum(arr_sum)))