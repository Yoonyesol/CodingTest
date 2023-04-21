import sys
n, s, r = map(int, sys.stdin.readline().split())
temp = []
kayac = [0 for _ in range(n+2)]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(s):
    kayac[temp[i]] -= 1
temp = list(map(int, sys.stdin.readline().split()))
for i in range(r):
    kayac[temp[i]] += 1
for i in range(1, len(kayac)):
    if kayac[i] == 1:
        if kayac[i-1] == -1:
            kayac[i-1] += 1
            kayac[i] -= 1
        elif kayac[i+1] == -1:
            kayac[i+1] += 1
            kayac[i] -= 1
print(kayac.count(-1))