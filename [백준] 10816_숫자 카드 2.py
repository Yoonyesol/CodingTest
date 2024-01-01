import sys
input = sys.stdin.readline

n = int(input().rstrip())
card = list(map(int, input().split()))
m = int(input().rstrip())
card2 = list(map(int, input().split()))

dic = dict()
for i in card:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

for i in card2:
    if i in dic.keys():
        print(dic[i], end=" ")
    else:
        print(0, end=" ")

--------------------------------

import sys
input = sys.stdin.readline

n = int(input().rstrip())
card = list(map(int, input().split()))
m = int(input().rstrip())
card2 = list(map(int, input().split()))

result = [0] * 20000001
for i in card:
    result[i+10000000] += 1

for i in card2:
    print(result[i+10000000], end=" ")