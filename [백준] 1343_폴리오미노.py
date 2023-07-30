import sys
input=sys.stdin.readline
b = input().rstrip().split(".")
str = ''
for i in b:
    n = len(i)
    if n == 0:
        str += "."
        continue
    if n >= 4:
        str += "AAAA"*(n//4)
        n -= (4*(n//4))
    if n == 0:
        str += "."
        continue
    if n % 2 == 0:
        str += "BB"
    else:
        str = "-1"
        break
    str += "."
if str[-1] == ".":
    print(str[:-1])
else:
    print(str)

-----------------

import sys
input=sys.stdin.readline
b = input()
b = b.replace("XXXX", "AAAA")
b = b.replace("XX", "BB")
if "X" in b:
    print(-1)
else:
    print(b)
