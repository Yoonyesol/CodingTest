import sys
input = sys.stdin.readline

dic = dict()
total = 0
while True:
    n = input().strip()
    if not n:
        break
    total += 1

    if n not in dic.keys():
        dic[n] = 1
    else:
        dic[n] += 1

for i in sorted(dic.items(), key=lambda x:x[0]):
    print('%s %.4f' %(i[0], i[1] * 100 / total))