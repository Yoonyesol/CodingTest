import sys
input = sys.stdin.readline

n = int(input().rstrip())
checkList = []
for _ in range(n):
    a = list(input().split())
    if len(a) >= 2:
        num = int(a[1])
    if a[0] == "all":
        checkList = []
        for i in range(1, 21):
            checkList.append(i)
    elif a[0] == "empty":
        checkList = []
    elif a[0] == "add":
        if num not in checkList:
            checkList.append(num)
    elif a[0] == "remove":
        if num in checkList:
            checkList.remove(num)
    elif a[0] == "check":
        if num in checkList:
            print(1)
        else:
            print(0)
    elif a[0] == "toggle":
        if num in checkList:
            checkList.remove(num)
        else:
            checkList.append(num)