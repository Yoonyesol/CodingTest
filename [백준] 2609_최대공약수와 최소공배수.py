import sys, math
input=sys.stdin.readline
a_arr = set()
gcd = []
a, b = map(int, input().split())
for i in range(1, int(math.sqrt(a))+1):
    if a % i == 0:
        a_arr.add(i)
        a_arr.add(a//i)
for i in range(1, int(math.sqrt(b))+1):
    if b % i == 0:
        if i in a_arr:
            gcd.append(i)
        if b//i in a_arr:
            gcd.append(b//i)
print(max(gcd))
i = 1
while True:
    if (max(a, b) * i) % min(a, b) == 0:
        print((max(a, b) * i))
        break
    i += 1