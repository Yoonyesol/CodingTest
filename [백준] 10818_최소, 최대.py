import sys
input=sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr))