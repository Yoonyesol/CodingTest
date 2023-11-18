T = int(input())
for test_case in range(1, T + 1):
    D, H, M = map(int, input().split())

    appointmentTime = 11 * 24 * 60 + 11 * 60 + 11
    currentTime = D * 24 * 60 + H * 60 + M
    ans = currentTime - appointmentTime
    if ans < 0:
        ans = -1

    print(f'#{test_case} {ans}')