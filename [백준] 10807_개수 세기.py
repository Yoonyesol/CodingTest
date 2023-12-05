import sys
input = sys.stdin.readline

_ = int(input().rstrip())
arr = list(map(int, input().split()))
v = int(input().rstrip())

print(arr.count(v))