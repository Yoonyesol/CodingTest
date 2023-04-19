import sys
paper = int(sys.stdin.readline())
arr = [[0]*101 for _ in range(101)]
cnt = 0
for i in range(paper):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(b, b+10):
        for j in range(a, a+10):
            arr[i][j] = 1
for i in range(101):
    cnt += arr[i].count(1)
print(cnt)