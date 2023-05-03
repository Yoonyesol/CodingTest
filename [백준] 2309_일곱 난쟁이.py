import sys
input=sys.stdin.readline
arr = []
a, b = 0, 0
for _ in range(9):
    arr.append(int(input().rstrip()))
search = sum(arr) - 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j] == search:
            a = arr[i]
            b = arr[j]
            break
    if len(arr) == 7:
        break
for i in sorted(arr):
    if i == a or i == b:
        continue
    print(i)
