T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')