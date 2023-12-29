import sys
input = sys.stdin.readline

n = int(input().strip())
total = 0
#n이 5의 배수가 될 때까지 n에서 3을 뺀다.
while n >= 0:
    if n % 5 == 0:
        total += n // 5
        print(total)
        break
    n -= 3
    total += 1
else:   #n이 0보다 크거나 같은 동안에 5의 배수가 되지 않는다면, 3,5로 나타낼 수 없는 수이다.
    print(-1)