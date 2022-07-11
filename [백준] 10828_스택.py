import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        arr.append(cmd[1])
    elif cmd[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:    
            print(int(arr[-1]))
    elif cmd[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(int(arr[-1]))
            arr.pop()
    elif cmd[0] == "size":
        print(len(arr))