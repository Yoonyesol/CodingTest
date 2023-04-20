import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
if n <= 25:
    print(s)
elif n > 25:
    if "." not in s[11:-12]:
        a = s[:11]
        b = "..."
        c = s[-11:]
    else:
        a = s[:9]
        b = "......"
        c = s[-10:]
    print(a+b+c)