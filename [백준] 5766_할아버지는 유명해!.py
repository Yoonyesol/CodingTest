import sys
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    player = {}
    for _ in range(n):
        p = list(map(int, sys.stdin.readline().split()))
        for i in p:
            if i in player:
                player[i] += 1
            else:
                player[i] = 1
    player = sorted(player.items(), key = lambda x:(-x[1], x[0]))
    score = player[1][1]
    for i in player:
        if i[1] == score:
            print(i[0], end=' ')
    print()