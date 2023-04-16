import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())  #k층
    n = int(sys.stdin.readline())  #n호
    cnt = 1
    apt = [[0]*(n+1) for _ in range(k+1)]
    for i in range(k+1):
        answer = 0
        for j in range(1, n+1):
            if i == 0:
                apt[i][j] = j
            else:
                apt[i][j] = sum(apt[i-1][:j+1])
    print(apt[k][n])