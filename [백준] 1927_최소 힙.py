import sys, heapq
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    num = int(input().rstrip())
    if len(arr) == 0 and num == 0:
        print(0)
        continue
    if num == 0:
        print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, num)
