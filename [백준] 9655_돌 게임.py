import sys
n = int(sys.stdin.readline())
i = n // 3
n %= 3
i += n
if i % 2 == 1:
    print("SK")
else:
    print("CY")