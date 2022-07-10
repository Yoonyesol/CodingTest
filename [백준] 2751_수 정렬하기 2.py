import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    number = int(sys.stdin.readline())
    arr.append(number)
arr.sort()
for j in arr:
    print(j)