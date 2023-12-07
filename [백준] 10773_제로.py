import sys
input = sys.stdin.readline

k = int(input().rstrip())
arr = []

for _ in range(k):
    a = int(input().rstrip())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)

print(sum(arr))
