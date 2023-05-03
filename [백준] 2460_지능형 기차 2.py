import sys
input=sys.stdin.readline
maxP = 0
people = 0
for _ in range(10):
    outT, inT = map(int, input().split())
    people -= outT
    people += inT
    if maxP < people:
        maxP = people
print(maxP)