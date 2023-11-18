T = int(input())
for test_case in range(1, T + 1):
    n = int(input().rstrip())
    bus = [0 for _ in range(5001)]

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bus[i] += 1

    p = int(input().rstrip())
    ans = []
    for _ in range(p):
        a = int(input().rstrip())
        ans.append(bus[a])
    ans = ' '.join(map(str, ans))

    print(f'#{test_case} {ans}')