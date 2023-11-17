T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    boxes = [0 for _ in range(n+1)]

    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            boxes[j] = i
            
    ans = ' '.join(map(str, boxes[1:]))
    print(f'#{test_case} {ans}')