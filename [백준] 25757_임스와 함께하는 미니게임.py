import sys
n, p = sys.stdin.readline().split()
player = set()
ims_p = {"Y":1, "F":2, "O":3}
for _ in range(int(n)):
    player.add(sys.stdin.readline().rstrip())
print(len(player)//ims_p[p])