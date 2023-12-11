import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = deque()
for _ in range(n):
    a = list(input().split())

    if a[0] == 'push_back':
        arr.append(int(a[1]))
    elif a[0] == 'push_front':
        arr.insert(0, int(a[1]))
    elif a[0] == 'pop_back':
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif a[0] == 'pop_front':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif a[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)