import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    arr = []
    n = int(input())
    while n > 0:
        arr.append(n % 2)
        n = n // 2
    for i in range(len(arr)):
        if arr[i] == 1:
            print(i, end=" ")