import sys
input = sys.stdin.readline

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alp = input().rstrip()

for i in croatia:
    if i in alp:
        alp = alp.replace(i, "1")
print(len(alp))