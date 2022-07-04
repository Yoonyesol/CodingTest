import sys
import itertools
n, m = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
answer = []
compList = list(itertools.combinations(data, 3))
for i in compList:
    if sum(i) <= m:
        answer.append(sum(i))
print(max(answer))  