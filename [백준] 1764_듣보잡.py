import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a_set = set()
b_set = set()
for _ in range(a):
    a_set.add(input().rstrip())
for _ in range(b):
    b_set.add(input().rstrip())
c = list(a_set & b_set)
print(len(c))
for i in sorted(c):
    print(i)