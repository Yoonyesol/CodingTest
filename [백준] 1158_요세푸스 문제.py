import sys
n, p = map(int, sys.stdin.readline().split())
idx = 0
stack = [i+1 for i in range(n)]
answer = []
while stack:
    idx = (idx + (p - 1)) % len(stack)
    answer.append(stack.pop(idx))
print("<%s>" % ", ".join(map(str, answer)))