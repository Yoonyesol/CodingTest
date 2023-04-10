import sys

a, k = map(int, sys.stdin.readline().split())
answer = 0

while k > 0:
    if a == k:
        print(answer)
        break
    else:
        if k // 2 >= a:
            if k % 2 == 0:
                k = k // 2
            else:
                k -= 1
            answer += 1
        elif k - 1 >= a:
            k -= 1
            answer += 1