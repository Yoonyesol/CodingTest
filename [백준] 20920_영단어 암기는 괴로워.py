import sys
input=sys.stdin.readline

n, m = map(int, input().split())
dic = dict()

for i in range(n):
    a = input().rstrip()
    if len(a) >= m:
        if a not in dic.keys():
            dic[a] = 0
        else:
            dic[a] += 1

sortedDic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))    #카운팅수, 단어길이, 알파벳 순으로 정렬
for i in sortedDic:
    print(i[0])
