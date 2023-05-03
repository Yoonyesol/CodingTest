import sys, math
input=sys.stdin.readline
arr = set()
n, k = map(int, input().split())
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        arr.add(i)
        arr.add(n//i)
if len(arr) < k:
    print(0)
else:
    arr = sorted(arr)
    print(arr[k-1])