import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    ans = []
    record = list(input().split())
    animal = []
    while True:
        a = list(input().split())
        if len(a) != 3:
            break
        animal.append(a[2])
    for i in record:
        if i not in animal:
            ans.append(i)
    print(' '.join(ans))