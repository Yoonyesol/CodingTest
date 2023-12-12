import sys
input = sys.stdin.readline

a = int(input().rstrip())
sumN = 1
for i in range(1, a+1):
    sumN *= i
print(sumN)