import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = dict()
for _ in range(n):
    _, b = input().rstrip().split(".")
    if b not in dic.keys():
        dic[b] = 1
    else:
        dic[b] += 1
for i in sorted(dic.items(), key=lambda x:x[0]):
    print(i[0], i[1])